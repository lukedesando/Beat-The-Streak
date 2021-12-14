-- SELECT 
-- 	PlayerName,
--     MLBID,
--     H,
--     `Date`,
--     `Year`
-- from
--     DatabaseBatterGamelogs;



-- Alter TABLE TestTable add lTEST SMALLINT;

-- select concat(h,k) from TestTable;

-- update TestTable set lTEST = concat(h,k);



-- select concat(`Date`,' ',`Year`) FROM DatabaseBatterGamelogs;

Alter Table DatabaseBatterGamelogs add FullDate date;
Alter Table DatabasePitcherGamelogs add FullDate date;

update DatabaseBatterGamelogs set FullDate = concat(GameDate,', ',GameYear);
update DatabasePitcherGamelogs set FullDate = concat(GameDate,', ',GameYear);

select str_to_date('May 30 2021', '%M %e %Y');

update DatabaseBatterGamelogs set FullDate = replace(FullDate, FullDate,str_to_date(FullDate, '%M %e, %Y'));

-- Alter table DatabaseBatterGamelogs drop FullDate;
-- Alter table DatabasePitcherGamelogs drop FullDate;

select FullDate from DatabaseBatterGamelogs
where FullDate LIKE '%(2)%';

-- Update DatabaseBatterGamelogs set DubHeadGame =

select GameDate, instr(GameDate,'(')+1 as DoubleDouble from DatabaseBatterGamelogs;
and set DoubleStart = DoubleDouble;

alter Table DatabaseBatterGamelogs add DoubleStart TinyInt;
Alter table DatabaseBatterGamelogs set DoubleStart = instr(GameDate,'(');

select GameDate, FullDate, SUBSTRING(GameDate,instr(GameDate,'(')+1,1) as GameNum from DatabaseBatterGamelogs where GameDate like '%(%';

alter table DatabaseBatterGamelogs add DoubleStart AS SUBSTRING(GameDate,instr(GameDate,'(')+1,1) as GameNum where GameDate like '%(%';

alter table TestTable add COLUMN MTest TEXT;
alter table TestTable add column NTest TEXT;
update TestTable set MTest = instr(lTEST,'8');
update TestTable set NTest = Substring(lTEST,instr(lTEST,'8'),1);


update DatabasePitcherGamelogs set DoubleHeadGame = SUBSTRING(GameDate,instr(GameDate,'(')+1,1) where GameDate like '%(%';

alter table DatabaseBatterGamelogs add column Suspended TEXT;
alter table DatabasePitcherGamelogs add column Suspended TEXT;

update DatabaseBatterGamelogs set Suspended = 'Suspended' where GameDate like '%susp%';
update DatabasePitcherGamelogs set Suspended = 'Suspended' where GameDate like '%susp%';