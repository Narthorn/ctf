library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.galois_field.all;

--------------------------------------------
-- Operations dans GF(32)
-- avec le polynome : X^5+ X^2 +1
--------------------------------------------

entity evil_cipher is
  port (
    clk    : in  std_logic;
    resetn : in  std_logic;
    start  : in  std_logic;
    key    : in  std_logic_vector(63 downto 0);
    din    : in  std_logic_vector(44 downto 0);
    dout   : out std_logic_vector(44 downto 0);
    ready  : out std_logic 
  );
end entity;

architecture rtl of evil_cipher is
  type state is (idle, cipher);
  signal current_state : state;
  signal next_state    : state;
  signal reg_data      : std_logic_vector(din'range);
  signal rkey          : std_logic_vector(din'range);
  signal ctr           : natural range 0 to 5;
  signal load          : std_logic;
  signal busy          : std_logic;
  
begin
 ready <= not busy;
 dout <= (others => '0') when busy = '1'
         else reg_data;
 
 process(clk,resetn) is
 begin
   if resetn = '0' then
     current_state <= idle;     
     reg_data <= (others => '0');
     ctr      <= 0;
    
   elsif rising_edge(clk) then
     -- state register
     current_state <= next_state;
     
     -- counter
     if busy = '0' or ctr=5 then 
       ctr <= 0;
     else
       ctr <= ctr+1;
     end if;
     
     -- data register
     if busy = '1' then 
       if ctr = 0 then
         reg_data <= rkey xor reg_data;
       else 
          reg_data <= round(reg_data,rkey);
       end if;
     elsif load = '1' then 
       reg_data <= din;
     end if;
   end if; 
 end process;
 
 exp : entity work.key_expansion 
   port map (
     resetn => resetn,
     clk    => clk,
     load   => load,
     key    => key,
     rkey   => rkey
   );
   
   process (current_state, start, ctr) is
   begin
     case current_state is
       when idle =>
         if start = '1' then 
           next_state <= cipher;  
         else
           next_state <= idle;  
         end if;
         busy <= '0';
         load <= start;
       when cipher =>
         if ctr < 5 then 
           next_state <= cipher;  
         else
           next_state <= idle;  
         end if;
         busy <= '1';
         load <= '0';        
     end case;
   end process;

 
end architecture;

