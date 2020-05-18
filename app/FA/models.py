from django.db import models

# Create your models here.
#机种名称
class ProjectsName(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50,null=False)                               # 机种名称
    CreateTime = models.DateTimeField(auto_now_add=True,blank=True)                  # 创建时间
    UpdatedTime = models.DateTimeField(null=True,blank=True)                         # 更新时间
    class Meta:
        db_table = 'ProjectsName'
        ordering = ['Id']
    def __str__(self):
        return 'Id%s: Name(%s),CreateTime(%s),UpdatedTime(%s)'% (self.Id,self.Name,self.CreateTime,self.UpdatedTime)


#客户名称
class Customers(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50,null=False)                               # 客户名称
    CreateTime = models.DateTimeField(auto_now_add=True,blank=True)                  # 创建时间
    UpdatedTime = models.DateTimeField(null=True,blank=True)                         # 更新时间
    class Meta:
        db_table = 'Customers'
        ordering = ['Id']
    def __str__(self):
        return 'Id%s: Name(%s),CreateTime(%s),UpdatedTime(%s)'% (self.Id,self.Name,self.CreateTime,self.UpdatedTime)
#所属BU
class BU(models.Model):
    Id = models.BigAutoField(primary_key=True)
    BUName = models.CharField(max_length=50,null=False)                             # 所属BU
    CreateTime = models.DateTimeField(auto_now_add=True,blank=True)                  # 创建时间
    UpdatedTime = models.DateTimeField(null=True,blank=True)                         # 更新时间
    class Meta:
        db_table = 'BU'
        ordering = ['Id']
    def __str__(self):
        return 'Id%s: BUName(%s),CreateTime(%s),UpdatedTime(%s)'% (self.Id,self.BUName,self.CreateTime,self.UpdatedTime)
#治具厂商
class EquipmentVendor(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Vendor = models.CharField(max_length=50,null=False)                             # 治具厂商
    CreateTime = models.DateTimeField(auto_now_add=True,blank=True)                  # 创建时间
    UpdatedTime = models.DateTimeField(null=True,blank=True)                         # 更新时间
    class Meta:
        db_table = 'EquipmentVendor'
        ordering = ['Id']
    def __str__(self):
        return 'Id%s: Vendor(%s),CreateTime(%s),UpdatedTime(%s)'% (self.Id,self.Vendor,self.CreateTime,self.UpdatedTime)
#治具类型
class EquipmentType(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Type = models.CharField(max_length=50,null=False)                               # 治具类型
    CreateTime = models.DateTimeField(auto_now_add=True,blank=True)                  # 创建时间
    UpdatedTime = models.DateTimeField(null=True,blank=True)                         # 更新时间
    class Meta:
        db_table = 'EquipmentType'
        ordering = ['Id']
    def __str__(self):
        return 'Id%s: Type(%s),CreateTime(%s),UpdatedTime(%s)'% (self.Id,self.Type,self.CreateTime,self.UpdatedTime)
#站别
class Station(models.Model):
    Id = models.BigAutoField(primary_key=True)
    StationLine = models.CharField(max_length=50,null=False)                        # 站别
    CreateTime = models.DateTimeField(auto_now_add=True,blank=True)                  # 创建时间
    UpdatedTime = models.DateTimeField(null=True,blank=True)                         # 更新时间
    class Meta:
        db_table = 'Station'
        ordering = ['Id']
    def __str__(self):
        return 'Id%s: StationLine(%s),CreateTime(%s),UpdatedTime(%s)'% (self.Id,self.StationLine,self.CreateTime,self.UpdatedTime)
#问题归类
class QuestionClass(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Classify = models.CharField(max_length=50,null=False)                           # 问题归类
    CreateTime = models.DateTimeField(auto_now_add=True,blank=True)                  # 创建时间
    UpdatedTime = models.DateTimeField(null=True,blank=True)                         # 更新时间
    class Meta:
        db_table = 'QuestionClass'
        ordering = ['Id']
    def __str__(self):
        return 'Id%s: Classify(%s),CreateTime(%s),UpdatedTime(%s)'% (self.Id,self.Classify,self.CreateTime,self.UpdatedTime)




#Equipment Number
class EquipmentNumber(models.Model):
    Id = models.BigAutoField(primary_key=True)                                       # Id
    EquipmentNo = models.CharField(max_length=50, null=False)                        # 治具编号
    ProjectName = models.CharField(max_length=50, null=True,blank=True)              # 机种名称
    Customer = models.CharField(max_length=50, null=True,blank=True)                 # 客户名称
    BringToBU = models.CharField(max_length=50, null=True,blank=True)                # 所属BU
    EquipmentVendor = models.CharField(max_length=50, null=True,blank=True)          # 治具厂商
    EquipmentType = models.CharField(max_length=50, null=True,blank=True)            # 治具类型
    StationLine = models.CharField(max_length=50, null=True,blank=True)              # 站别
    CreateTime = models.DateTimeField(auto_now_add=True)                             # 创建时间
    UpdatedTime = models.DateTimeField(null=True,blank=True)                         # 更新时间
    class Meta:
        db_table = 'EquipmentNumber'
        ordering = ['Id']
    def __str__(self):
        return 'Id%s: EquipmentNo(%s),ProjectName(%s),Customer(%s),BringToBU(%s)' \
               ',EquipmentVendor(%s),EquipmentType(%s),StationLine(%s),CreateTime(%s),UpdatedTime(%s)' \
               % (self.Id,self.EquipmentNo,self.ProjectName,self.Customer,self.BringToBU
                  ,self.EquipmentVendor,self.EquipmentType,self.StationLine,self.CreateTime,self.UpdatedTime)

#FA analysis
class FAMode(models.Model):
    Id = models.BigAutoField(primary_key=True)                                       # Id
    EquipmentNo = models.CharField(max_length=50, null=False)                        # 治具编号
    Line = models.CharField(max_length=50,null=True,blank=True)                      # 线别
    StationLine = models.CharField(max_length=50, null=True,blank=True)              # 站别
    QuestionDesc = models.CharField(max_length=500, null=True,blank=True)            # 问题描述
    EssentialIssues = models.CharField(max_length=500,null=True,blank=True)          # 根本原因
    Solution = models.CharField(max_length=500,null=True,blank=True)                 # 解决方法
    RepairTime = models.IntegerField(default=0,null=True,blank=True)                 # 修复时长以分钟计算
    QuestionClassify = models.CharField(max_length=50,null=True,blank=True)          # 问题归类
    QuestionDate = models.DateTimeField(null=True,blank=True)
    Analyst = models.CharField(max_length=50, null=True,blank=True)                  # 分析员
    AttachmentPath = models.CharField(max_length=500,null=True)                      # 分析报告存放的路径
    Remark = models.CharField(max_length=200, null=True, blank=True)                 # 备注信息

    CreateTime = models.DateTimeField(auto_now_add=True)                             # 创建时间
    UpdatedTime = models.DateTimeField(null=True,blank=True)                         # 更新时间
    class Meta:
        db_table = 'FAMode'
        ordering = ['Id']
    def __str__(self):
        return 'Id%s: EquipmentNo(%s),Line(%s),StationLine(%s),QuestionDesc(%s)' \
               ',EssentialIssues(%s),RepairTime(%s),QuestionClassify(%s),Analyst(%s),AttachmentPath(%s),Remark(%s),CreateTime(%s),UpdatedTime(%s)' \
               % (self.Id,self.EquipmentNo,self.Line,self.StationLine,self.QuestionDesc
                  ,self.EssentialIssues,self.RepairTime,self.QuestionClassify,self.Analyst,self.AttachmentPath,self.Remark,self.CreateTime,self.UpdatedTime)