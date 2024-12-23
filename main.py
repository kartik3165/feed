import feedparser
import pywhatkit as kit
import time

# Function to fetch RSS feed
def fetch_rss():
    rss_url = 'https://steveblank.com/feed/'
    feed = feedparser.parse(rss_url)
    latest_entry = feed.entries[0]
    return latest_entry.title, latest_entry.link

# Function to send WhatsApp message
def send_whatsapp_message(message):
    # Replace with your group or contact number
    group_number = "FPVLggqhoTQHHZXJ05scAp"
    kit.sendwhatmsg_to_group(group_number, message, time.localtime().tm_hour, time.localtime().tm_min + 1)

# Main function to automate the process
def send_daily_update():
    title, link = fetch_rss()
    message = f"Daily Update: {title}\n{link}"
    send_whatsapp_message(message)

# Schedule daily message (run it at 9 AM every day)
while True:
    current_time = time.localtime()
    if current_time.tm_hour == 9 and current_time.tm_min == 0:
        send_daily_update()
        time.sleep(60)  # Sleep for 1 minute to avoid multiple executions
    time.sleep(30)  # Check every 30 seconds
