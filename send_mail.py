import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自Luke的测试邮件', 'Luke2021_keep@163.com', '964985736@qq.com'
    text_content = '欢迎访问Django，这里是Django的邮箱测试验证！'
    html_content = '专注于Python、Django和机器学习技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
