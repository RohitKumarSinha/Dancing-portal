from django.db import models

# Create your models here.

class upload_video(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=40, null=False) #phone
    desc = models.CharField(max_length=305, null=False)
    url = models.CharField(max_length=100, null=False)
    status = models.BooleanField(default=False)
    votes = models.IntegerField(max_length=4, default = 0)
    rating = models.FloatField(max_length=4, default=0.0)

    class Meta:
        managed = False
        db_table = 'upload_video'
        verbose_name = 'upload_video'
        verbose_name_plural = 'upload_videos'

    def __str__(self):
        return self.name
    

'''        
desc upload_video;
	
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| email  | varchar(50)  | YES  |     | NULL    |                |
| name   | varchar(40)  | YES  |     | NULL    |                |
| desc   | varchar(350) | YES  |     | NULL    |                |
| url    | varchar(105) | YES  |     | NULL    |                |
| status | int          | NO   |     | 0       |                |
| rating | float(4,2)   | YES  |     | 0.00    |                |
| votes  | int          | YES  |     | 0       |                |
+--------+--------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)

'''
