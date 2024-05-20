from apscheduler.schedulers.background import BackgroundScheduler

def avansas_rival_analysis_job():
    print("Avansas rival analysis completed")

def ofmark_rival_analysis_job():
    print("Ofmark rival analysis completed")

# Zamanlayıcıyı başlat
scheduler = BackgroundScheduler()
scheduler.add_job(avansas_rival_analysis_job, 'cron', hour=5)  # Her gün gece yarısı çalıştır
scheduler.add_job(ofmark_rival_analysis_job, 'cron', hour=5, minute=30) # Her gün gece 00:30 çalıştır
scheduler.start()
