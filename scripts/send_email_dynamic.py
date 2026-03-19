import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(title, url, to_email):
    api_key = os.environ.get('SENDGRID_API_KEY')
    if not api_key:
        raise ValueError("SENDGRID_API_KEY environment variable is not set")

    sg = SendGridAPIClient(api_key)
    message = Mail(
        from_email=os.environ.get('SENDGRID_FROM_EMAIL', 'noreply@example.com'),
        to_emails=to_email,
        subject=f"New blog post: {title}"
    )
    message.template_id = os.environ.get('SENDGRID_TEMPLATE_ID')
    message.dynamic_template_data = {'title': title, 'url': url}

    try:
        response = sg.send(message)
        print(f"Email sent successfully with status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise

if __name__ == '__main__':
    main(
'Daily AI Insight: A Practical Quickstart',
'https://blog-vercel-lake.vercel.app/posts/2026-03-20-daily-ai-insight',
os.environ['EMAIL_TO']
)