-- select concat(`Date`,' ',`Year`) FROM DatabaseBatterGamelogs;

Alter Table DatabaseBatterGamelogs add GameDate TEXT;
Alter Table DatabasePitcherGamelogs add GameDate TEXT;

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

-- select GameDate, FullDate, SUBSTRING(GameDate,instr(GameDate,'(')+1,1) as GameNum from DatabaseBatterGamelogs where GameDate like '%(%';

-- alter table DatabaseBatterGamelogs add DoubleStart AS SUBSTRING(GameDate,instr(GameDate,'(')+1,1) as GameNum where GameDate like '%(%';

alter table TestTable add column MTest TEXT;
alter table TestTable add column NTest TEXT;
update TestTable set MTest = instr(lTEST,'8');
update TestTable set NTest = Substring(lTEST,instr(lTEST,'8'),1);




alter table DatabaseBatterGamelogs add column Suspended TEXT;
alter table DatabasePitcherGamelogs add column Suspended TEXT;

-- update DatabaseBatterGamelogs set Suspended = 'Suspended' where RawGameDate like '%susp%';
-- update DatabasePitcherGamelogs set Suspended = 'Suspended' where RawGameDate like '%susp%';

-- select RawGameDate, replace(RawGameDate,' susp','') as TestyTesty from DatabaseBatterGamelogs where RawGameDate like '%susp%';




-- UPDATE DatabaseBatterGamelogs set GameDate = RawGameDate;
-- UPDATE DatabasePitcherGamelogs set GameDate = RawGameDate;

-- alter Table DatabaseBatterGamelogs add DoubleHeadGame TinyInt;
-- alter Table DatabaseBatterGamelogs add DoubleHeadGame TinyInt;
-- update DatabaseBatterGamelogs set DoubleHeadGame = SUBSTRING(GameDate,instr(GameDate,'(')+1,1) where GameDate like '%(%';
-- update DatabasePitcherGamelogs set DoubleHeadGame = SUBSTRING(GameDate,instr(GameDate,'(')+1,1) where GameDate like '%(%';

-- update DatabaseBatterGamelogs set GameDate = replace(RawGameDate,'(1)','') where RawGameDate like '%(1)%';
-- update DatabasePitcherGamelogs set GameDate = replace(RawGameDate,'(1)','') where RawGameDate like '%(1)%';
-- update DatabaseBatterGamelogs set GameDate = replace(RawGameDate,'(2)','') where RawGameDate like '%(2)%';
-- update DatabasePitcherGamelogs set GameDate = replace(RawGameDate,'(2)','') where RawGameDate like '%(2)%';
-- update DatabaseBatterGamelogs set GameDate = replace(RawGameDate,' susp','') where RawGameDate like '%susp%';
-- update DatabasePitcherGamelogs set GameDate = replace(RawGameDate,' susp','') where RawGameDate like '%susp%';

-- alter table DatabaseBatterGamelogs add column Suspended TEXT;
-- alter table DatabasePitcherGamelogs add column Suspended TEXT;
-- update DatabaseBatterGamelogs set Suspended = 'Suspended' where RawGameDate like '%susp%';
-- update DatabasePitcherGamelogs set Suspended = 'Suspended' where RawGameDate like '%susp%';
-- update DatabaseBatterGamelogs set FullDate = concat(GameDate,', ',GameYear);
-- update DatabasePitcherGamelogs set FullDate = concat(GameDate,', ',GameYear);

-- alter table DatabaseBatterGamelogs add column game_date date;
-- alter table DatabasePitcherGamelogs add column game_date date;
-- update DatabaseBatterGamelogs set game_date = replace(FullDate, FullDate,str_to_date(FullDate, '%M %e, %Y'));
-- update DatabasePitcherGamelogs set game_date = replace(FullDate, FullDate,str_to_date(FullDate, '%M %e, %Y'));

-- select RawGameDate, Suspended from DatabasePitcherGamelogs where RawGameDate like '%susp%';
-- select FullDate, replace(FullDate, FullDate,str_to_date(FullDate, '%M %e, %Y')) as game_date from DatabasePitcherGamelogs;