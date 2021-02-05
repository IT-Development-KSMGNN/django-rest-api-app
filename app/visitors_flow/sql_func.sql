-- Группы
alter FUNCTION dbo.collect_data 
(
	@start date,
	@end date,
	@mall int
)
RETURNS 
@result TABLE 
(
	[date]		date,
	[realin]	int,
	[realout]	int,
	[mall]		int
)
AS
BEGIN
	insert into @result
	Select 
		[date]
		,[realin]
		,[realout]
		,@mall as [mall]
	from (
	SELECT CAST(DateCreated as DATE) as [date], SUM(RealIn) as [realin], SUM(RealOut) as [realout]
			FROM [Traffic] 
			WHERE cast(DateCreated as date)
			BETWEEN @start and @end 
			and ([SensorID] in (select Sensors.ID from Sensors, Groups, GroupsEntries WHERE Groups.Name LIKE 'Входная группа%' and Groups.ID = GroupsEntries.GroupID and GroupsEntries.EntryID = Sensors.EntryID and Sensors.DeviceID != '')) and ((RealIn <> 0) or (RealOut <> 0)) 
			GROUP BY CAST(DateCreated as DATE)) as b
			order by 
			[date]
			
	RETURN 
END
GO


-- Зоны
alter FUNCTION dbo.collect_data 
(
	@start date,
	@end date,
	@mall int
)
RETURNS 
@result TABLE 
(
	[date]		date,
	[realin]	int,
	[realout]	int,
	[mall]		int
)
AS
BEGIN
	insert into @result
	Select 
		[date]
		,[realin]
		,[realout]
		,@mall as [mall]
	from (
	SELECT CAST(DateCreated as DATE) as [date], SUM(RealIn) as [realin], SUM(RealOut) as [realout]
			FROM [Traffic] 
			WHERE cast(DateCreated as date)
			BETWEEN @start and @end 
			and ([SensorID] in (select Sensors.ID from Sensors, Zones, ZoneEntries WHERE Zones.Name LIKE 'Входная группа%' and Zones.ID = ZoneEntries.ZoneID and ZoneEntries.EntryID = Sensors.EntryID and Sensors.DeviceID != '')) and ((RealIn <> 0) or (RealOut <> 0)) 
			GROUP BY CAST(DateCreated as DATE)) as b
			order by 
			[date]
			
	RETURN 
END
GO
