from django.db import models

# Create your models here.

class upload_video(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=40, null=True)
    desc = models.CharField(max_length=305, null=True)
    url = models.CharField(max_length=100, null=False)
    status = models.BooleanField(default=False)
    votes = models.IntegerField(max_length=4, default=0)
    rating = models.FloatField(max_length=4, default=0.0)
    video_id = models.CharField(max_length=20, null=False)

    class Meta:
        managed = False
        db_table = 'upload_video'
        verbose_name = 'upload_video'
        verbose_name_plural = 'upload_videos'

'''        
desc upload_video;
	
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| email    | varchar(50)  | YES  |     | NULL    |                |
| name     | varchar(40)  | YES  |     | NULL    |                |
| desc     | varchar(350) | YES  |     | NULL    |                |
| url      | varchar(105) | NO   |     | NULL    |                |
| status   | int          | NO   |     | 0       |                |
| video_id | varchar(20)  | NO   |     | NULL    |                |
| rating   | float(4,2)   | NO   |     | 0.00    |                |
| votes    | int          | NO   |     | 0       |                |
+----------+--------------+------+-----+---------+----------------+
9 rows in set (0.00 sec)

'''

class user_rating(models.Model):
    id = models.AutoField(primary_key=True)
    rating = models.FloatField(max_length=4, default=0.0)
    mob_no = models.CharField(max_length=15, null=False)
    video = models.ForeignKey(upload_video, to_field= 'id', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'user_rating'
        verbose_name = 'user_rating'
        verbose_name_plural = 'user_ratings'


'''
desc user_rating;

+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| id       | int         | NO   | PRI | NULL    | auto_increment |
| rating   | float(4,2)  | NO   |     | 0.00    |                |
| mob_no   | varchar(15) | NO   |     | NULL    |                |
| video_id | varchar(20) | NO   | MUL | NULL    |                |
+----------+-------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

'''