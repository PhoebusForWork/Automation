DO $$

DECLARE
  last_dept_id INTEGER;
 
BEGIN
  SELECT id + 1 INTO last_dept_id FROM plt_account.vs_department ORDER BY id DESC LIMIT 1;
  EXECUTE 'ALTER SEQUENCE plt_account.vs_department_id_seq RESTART WITH ' || last_dept_id;


END $$;