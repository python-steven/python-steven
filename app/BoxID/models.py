from django.db import models
# Create your models here.

#Box information Form
class Box(models.Model):
    Id = models.BigAutoField(primary_key=True)
    BoxId = models.CharField(max_length=300,null=True)                               # BoxId
    ModelStageId = models.CharField(max_length=300,null=True,blank=True)             # modelStageId
    SerialNumberId = models.CharField(max_length=900,null=True,blank=True)           # SN的Id
    CreateTime = models.DateTimeField(auto_now_add=True,blank=True)                  # 创建时间
    UpdatedTime = models.DateTimeField(null=True,blank=True)                         # 更新时间
    class Meta:
        db_table = 'Box'
        ordering = ['-Id']
    def __str__(self):
        return 'Id%s: BoxId(%s),ModelStageId(%s),SerialNumberId(%s),CreateTime(%s),UpdatedTime(%s)' \
               % (self.Id,self.BoxId,self.ModelStageId,self.SerialNumberId,self.CreateTime,self.UpdatedTime)

#ModelStage information Form
class ModelStage(models.Model):
    Id = models.BigAutoField(primary_key=True)                                       # Id
    ModelStage = models.CharField(max_length=300, null=False)                        # ModelStage
    PartCode = models.CharField(max_length=300, null=True)                           # 料号
    PartName = models.CharField(max_length=300, null=True)                           # 品名
    RequireQuantity = models.IntegerField(null=True,default=0,blank=True)            # 需求数量
    BrushNumber = models.IntegerField(null=True,default=0,blank=True)                # 已刷数量
    AlternativeType = models.IntegerField(default=0,null=True,blank=True)            # 是否是代用料
    AlternativePartCode = models.CharField(max_length=900,null=True,blank=True)      # 代用料号
    Status = models.CharField(max_length=20, default='Open')                         # 状态
    CreateTime = models.DateTimeField(auto_now_add=True)                             # 创建时间
    UpdatedTime = models.DateTimeField(null=True,blank=True)                         # 更新时间
    class Meta:
        db_table = 'ModelStage'
        ordering = ['-Id']
    def __str__(self):
        return 'Id%s: ModelStage(%s),PartCode(%s),PartName(%s),RequireQuantity(%s)' \
               ',BrushNumber(%s),AlternativeType(%s),Status(%s),CreateTime(%s),UpdatedTime(%s)' \
               % (self.Id,self.ModelStage,self.PartCode,self.PartName,self.RequireQuantity
                  ,self.BrushNumber,self.AlternativeType,self.Status,self.CreateTime,self.UpdatedTime)

#SerialNumberInfo information Form
class SerialNumberInfo(models.Model):
    Id = models.BigAutoField(primary_key=True)
    SerialNumber = models.CharField(max_length=300, null=False)                    # SN
    PartCode = models.CharField(max_length=300, null=True,blank=True)              # 料号
    CreateTime = models.DateTimeField(auto_now_add=True)                           # 创建时间
    UpdatedTime = models.DateTimeField(null=True,blank=True)                       # 更新时间
    BoxIdBindingId = models.IntegerField(null=True,blank=True)                     # 绑定的BoxId
    class Meta:
        db_table = 'SerialNumberInfo'
        ordering = ['-Id']
    def __str__(self):
        return 'Id%s: SerialNumber(%s),PartCode(%s),CreateTime(%s),UpdatedTime(%s)' \
               % (self.Id,self.SerialNumber,self.PartCode,self.CreateTime,self.UpdatedTime)