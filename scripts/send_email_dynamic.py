import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(title, url, to_email):
    sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
    message = Mail(
    from_email=os.environ.get('SENDGRID_FROM_EMAIL', 'noreply@example.com'),
    to_emails=to_email,
    subject=f"New blog post: {title}"
    )
    message.dynamic_template_data = {'title': title, 'url': url}
    message.template_id = os.environ['SENDGRID_TEMPLATE_ID']
    sg.send(message)

if __name__ == '__main__':
    main(
'Daily AI Insight: A Practical Quickstart',
'https://your-vercel-site.vercel.app/posts/2026-03-20-daily-ai-insight',
os.environ['EMAIL_TO']
)