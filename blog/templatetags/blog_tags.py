from django import template
from django.db.models.aggregates import Count
from ..models import Post, Category, Tag

register = template.Library()

# 最新文章模板标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

# 归档模板标签
@register.simple_tag
def archives():
    # 这里 dates 方法会返回一个列表，
    # 列表中的元素为每一篇文章（Post）的创建时间，
    # 且是 Python 的 date 对象，精确到月份，降序排列。
    # 接受的三个参数：
    # 一个是 created_time ，即 Post 的创建时间，
    # month 是精度，
    # order='DESC' 表明降序排列（即离当前越近的时间越排在前面）
    return Post.objects.dates('created_time', 'month', order='DESC')

# 分类模板标签
@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

# 标签云
@register.simple_tag
def get_tags():
    # 记得在顶部引入 Tag model
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
