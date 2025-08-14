import io
import os
from contextlib import asynccontextmanager
from datetime import datetime, timezone

from dotenv import load_dotenv

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from PIL import Image, ImageDraw, ImageFont
from sqlalchemy import Column, create_engine, DateTime, Integer, String
from sqlalchemy.orm import declarative_base, Session, sessionmaker
from sqlalchemy.sql import func

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./profile_counter.db")

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class ProfileHit(Base):
    __tablename__ = "profile_hits"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    hit_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    last_hit = Column(DateTime, default=lambda: datetime.now(timezone.utc))


Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="GitHitBox",
    description="A reusable GitHub profile hit counter service that generates badge images",
    version="1.0.0",
    lifespan=lifespan,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_counter_badge(username: str, count: int, style: str = "flat") -> io.BytesIO:

    if style == "flat":
        height = 20
        padding = 6
        font_size = 11
        bg_color = "#555"
        count_bg_color = "#4c1"
        text_color = "#fff"
    elif style == "plastic":
        height = 18
        padding = 5
        font_size = 10
        bg_color = "#555"
        count_bg_color = "#97CA00"
        text_color = "#fff"
    elif style == "counter":
        height = 32
        padding = 4
        font_size = 16
        bg_color = "#2d3748"
        count_bg_color = "#2d3748"
        text_color = "#48bb78"
        digit_bg_color = "#1a202c"
        digit_border_color = "#4a5568"
    else:
        height = 28
        padding = 8
        font_size = 12
        bg_color = "#555"
        count_bg_color = "#4c1"
        text_color = "#fff"
    label_text = "Profile Views"
    count_text = str(count)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    if style == "counter":
        return create_counter_style_badge(
            count,
            font,
            height,
            padding,
            font_size,
            bg_color,
            text_color,
            digit_bg_color,
            digit_border_color,
        )
    label_bbox = font.getbbox(label_text)
    count_bbox = font.getbbox(count_text)

    label_width = label_bbox[2] - label_bbox[0]
    count_width = count_bbox[2] - count_bbox[0]

    total_width = label_width + count_width + (padding * 4)

    img = Image.new("RGB", (total_width, height), color="white")
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, label_width + padding * 2, height], fill=bg_color)
    draw.text(
        (padding, (height - font_size) // 2), label_text, fill=text_color, font=font
    )

    draw.rectangle(
        [label_width + padding * 2, 0, total_width, height], fill=count_bg_color
    )
    draw.text(
        (label_width + padding * 3, (height - font_size) // 2),
        count_text,
        fill=text_color,
        font=font,
    )

    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    return img_bytes


def create_counter_style_badge(
    count: int,
    font,
    height: int,
    padding: int,
    font_size: int,
    bg_color: str,
    text_color: str,
    digit_bg_color: str,
    digit_border_color: str,
) -> io.BytesIO:

    count_text = f"{count:07d}"
    digits = list(count_text)

    digit_width = 24
    digit_height = 24
    digit_spacing = 2
    total_digits = len(digits)

    digits_width = (digit_width * total_digits) + (digit_spacing * (total_digits - 1))
    total_width = digits_width

    img = Image.new("RGBA", (total_width, height), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    start_x = 0
    start_y = (height - digit_height) // 2

    for i, digit in enumerate(digits):
        x = start_x + (i * (digit_width + digit_spacing))
        y = start_y

        draw.rectangle(
            [x, y, x + digit_width, y + digit_height],
            fill="#0a0a0a",
            outline="#2a2a2a",
            width=1,
        )

        digit_bbox = font.getbbox(digit)
        digit_text_width = digit_bbox[2] - digit_bbox[0]
        digit_text_height = digit_bbox[3] - digit_bbox[1]

        text_x = x + (digit_width - digit_text_width) // 2
        text_y = y + (digit_height - digit_text_height) // 2 - digit_bbox[1] + 1

        draw.text((text_x, text_y), digit, fill="#00ff41", font=font)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    return img_bytes


@app.get("/")
async def root():
    return {
        "service": "GitHitBox",
        "version": "1.0.0",
        "usage": {
            "badge": "/badge/{username}",
            "count": "/count/{username}",
            "styles": ["flat", "plastic", "counter", "for-the-badge"],
        },
        "example": "https://your-domain.com/badge/octocat",
    }


@app.get("/badge/{username}")
async def get_profile_badge(
    username: str, style: str = "flat", db: Session = Depends(get_db)
):

    if not username or len(username) > 39:
        raise HTTPException(status_code=400, detail="Invalid username")
    if not all(c.isalnum() or c == "-" for c in username):
        raise HTTPException(status_code=400, detail="Invalid username format")
    profile_hit = db.query(ProfileHit).filter(ProfileHit.username == username).first()

    if profile_hit:
        profile_hit.hit_count += 1
        profile_hit.last_hit = datetime.now(timezone.utc)
    else:
        profile_hit = ProfileHit(username=username, hit_count=1)
        db.add(profile_hit)
    db.commit()

    img_bytes = create_counter_badge(username, profile_hit.hit_count, style)

    return StreamingResponse(
        io.BytesIO(img_bytes.read()),
        media_type="image/png",
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
        },
    )


@app.get("/count/{username}")
async def get_profile_count(username: str, db: Session = Depends(get_db)):

    if not username or len(username) > 39:
        raise HTTPException(status_code=400, detail="Invalid username")
    profile_hit = db.query(ProfileHit).filter(ProfileHit.username == username).first()

    if not profile_hit:
        return {"username": username, "count": 0, "message": "No hits recorded yet"}
    return {
        "username": username,
        "count": profile_hit.hit_count,
        "created_at": profile_hit.created_at.isoformat(),
        "last_hit": profile_hit.last_hit.isoformat(),
    }


@app.get("/stats")
async def get_global_stats(db: Session = Depends(get_db)):

    total_profiles = db.query(ProfileHit).count()
    total_hits = db.query(func.sum(ProfileHit.hit_count)).scalar() or 0

    return {
        "total_profiles": total_profiles,
        "total_hits": total_hits,
        "service": "GitHitBox",
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now(timezone.utc).isoformat()}


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 3001))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
