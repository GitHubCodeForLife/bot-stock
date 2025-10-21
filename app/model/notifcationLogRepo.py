from app.shareData import ShareData
from app.model.models import NotificationLog, db
from datetime import datetime

def add_notification_log(platform, channel, message, stock_code):
    with ShareData.app.app_context():
        log = NotificationLog(
            platform=platform,
            channel=channel,
            message=message,
            send_time=datetime.now(),
            stock_code=stock_code,
            type="price_alert"
        )
        db.session.add(log)
        db.session.commit()

def is_sent_notif_today(platform, channel, stock_code):
    with ShareData.app.app_context():
        today = datetime.now().date()
        log = NotificationLog.query.filter_by(
            platform=platform,
            channel=channel,
            stock_code=stock_code,
            type="price_alert"
        ).filter(db.func.date(NotificationLog.send_time) == today).first()
        return log is not None