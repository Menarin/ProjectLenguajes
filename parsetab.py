
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRIRCORCHETE ABRIRLLAVES ABRIRPARENTESIS BOOLEANO CERRARCORCHETE CERRARLLAVES CERRARPARENTESIS COMA DIVIDIR DOSPUNTOS ELSE EXCLAMACION FILTER IF IGUAL INT LAMBDA MAPA MAS MAYORQUE MENORQUE MENOS NUMERO OPERADORLOGICO POR PUNTOYCOMA REDUCE STR STRING VARIABLEassignVariable : VARIABLE IGUAL expr\n                    | VARIABLE IGUAL STRING\n                    | VARIABLE IGUAL lambda\n                    | VARIABLE IGUAL filter\n                    | VARIABLE IGUAL map\n                    | VARIABLE IGUAL reduce\n                    | VARIABLE IGUAL listalista : ABRIRCORCHETE lisString CERRARCORCHETE\n            | ABRIRCORCHETE lisInt CERRARCORCHETElisString : lisString COMA STRING\n                | STRINGlisInt : lisInt COMA NUMERO\n                | NUMEROcondicion : IGUAL IGUAL\n                | EXCLAMACION IGUAL\n                | MAYORQUE IGUAL\n                | MENORQUE IGUAL\n                | MAYORQUE\n                | MENORQUEevaluarCondicion : expr condicion expr\n                        | BOOLEANO\n                        | expr IGUAL IGUAL BOOLEANO\n                        | expr EXCLAMACION IGUAL BOOLEANO\n                        | evaluarCondicion OPERADORLOGICO evaluarCondicionexpr : expr MAS term\n            | ABRIRPARENTESIS expr MAS term CERRARPARENTESIS\n            | expr MENOS term\n            | ABRIRPARENTESIS expr MENOS term CERRARPARENTESIS\n            | termterm : term POR term\n            | term DIVIDIR term\n            | ABRIRPARENTESIS term POR NUMERO CERRARPARENTESIS\n            | ABRIRPARENTESIS term DIVIDIR NUMERO CERRARPARENTESIS\n            | NUMERO\n            | VARIABLE\n            | STRING\n            | ABRIRPARENTESIS term POR term CERRARPARENTESIS\n            | ABRIRPARENTESIS term DIVIDIR term CERRARPARENTESISparametros : parametros COMA VARIABLE\n                    | VARIABLE\n                    | parametros COMA assignVariable\n                    | assignVariable\n                    | cualquierCosa : STRING\n                    | NUMERO\n                    | VARIABLEmap : MAPA ABRIRPARENTESIS lambda COMA VARIABLE CERRARPARENTESIS\n            | MAPA ABRIRPARENTESIS lambda COMA lista CERRARPARENTESISfilter : FILTER ABRIRPARENTESIS lambda COMA VARIABLE CERRARPARENTESIS\n            | FILTER ABRIRPARENTESIS lambda COMA lista CERRARPARENTESISreduce : REDUCE ABRIRPARENTESIS lambda COMA VARIABLE CERRARPARENTESIS\n            | REDUCE ABRIRPARENTESIS lambda COMA lista CERRARPARENTESISlambda : LAMBDA parametros DOSPUNTOS expr\n            | LAMBDA parametros DOSPUNTOS evaluarCondicion\n            | LAMBDA parametros DOSPUNTOS INT IF evaluarCondicion ELSE cualquierCosa\n            | LAMBDA parametros DOSPUNTOS STR IF evaluarCondicion ELSE cualquierCosafilter : FILTER errorassignVariable : VARIABLE IGUAL expr error'
    
_lr_action_items = {'VARIABLE':([0,3,13,14,21,22,23,24,40,44,45,46,47,48,49,71,72,73,82,85,86,87,88,89,97,98,99,100,113,114,],[2,4,4,29,4,4,4,4,4,4,4,4,4,4,69,90,92,94,4,-18,-19,4,4,4,-14,-15,-16,-17,118,118,]),'$end':([1,4,5,6,7,8,9,10,11,12,19,20,27,32,39,41,42,43,53,55,64,65,68,76,77,78,79,80,81,96,101,105,106,107,108,109,110,111,112,115,116,117,118,119,],[0,-35,-1,-2,-3,-4,-5,-6,-7,-29,-34,-58,-36,-57,-25,-27,-30,-31,-8,-9,-53,-54,-21,-26,-28,-37,-32,-38,-33,-20,-24,-49,-50,-47,-48,-51,-52,-22,-23,-55,-44,-45,-46,-56,]),'IGUAL':([2,4,12,19,27,29,39,41,42,43,64,69,76,77,78,79,80,81,83,84,85,86,102,],[3,-35,-29,-34,-36,3,-25,-27,-30,-31,83,3,-26,-28,-37,-32,-38,-33,97,98,99,100,83,]),'STRING':([3,13,18,21,22,23,24,40,44,45,46,47,48,54,82,85,86,87,88,89,97,98,99,100,113,114,],[6,27,37,27,27,27,27,27,27,27,27,27,27,74,27,-18,-19,27,27,27,-14,-15,-16,-17,116,116,]),'ABRIRPARENTESIS':([3,13,15,16,17,21,22,23,24,40,44,45,46,47,48,82,85,86,87,88,89,97,98,99,100,],[13,13,31,33,34,40,40,40,40,40,40,40,40,40,13,13,-18,-19,13,13,13,-14,-15,-16,-17,]),'LAMBDA':([3,31,33,34,],[14,14,14,14,]),'FILTER':([3,],[15,]),'MAPA':([3,],[16,]),'REDUCE':([3,],[17,]),'ABRIRCORCHETE':([3,71,72,73,],[18,18,18,18,]),'NUMERO':([3,13,18,21,22,23,24,40,44,45,46,47,48,56,82,85,86,87,88,89,97,98,99,100,113,114,],[19,19,38,19,19,19,19,19,19,19,61,63,19,75,19,-18,-19,19,19,19,-14,-15,-16,-17,117,117,]),'POR':([4,6,12,19,26,27,39,41,42,43,57,58,59,60,61,62,63,78,79,80,81,],[-35,-36,23,-34,46,-36,23,23,23,23,46,23,23,23,-34,23,-34,-37,-32,-38,-33,]),'DIVIDIR':([4,6,12,19,26,27,39,41,42,43,57,58,59,60,61,62,63,78,79,80,81,],[-35,-36,24,-34,47,-36,24,24,24,24,47,24,24,24,-34,24,-34,-37,-32,-38,-33,]),'error':([4,5,6,12,15,19,27,39,41,42,43,76,77,78,79,80,81,],[-35,20,-36,-29,32,-34,-36,-25,-27,-30,-31,-26,-28,-37,-32,-38,-33,]),'MAS':([4,5,6,12,19,25,26,27,39,41,42,43,58,59,60,61,62,63,64,76,77,78,79,80,81,96,102,],[-35,21,-36,-29,-34,44,-29,-36,-25,-27,-30,-31,-25,-27,-30,-34,-31,-34,21,-26,-28,-37,-32,-38,-33,21,21,]),'MENOS':([4,5,6,12,19,25,26,27,39,41,42,43,58,59,60,61,62,63,64,76,77,78,79,80,81,96,102,],[-35,22,-36,-29,-34,45,-29,-36,-25,-27,-30,-31,-25,-27,-30,-34,-31,-34,22,-26,-28,-37,-32,-38,-33,22,22,]),'DOSPUNTOS':([4,5,6,7,8,9,10,11,12,14,19,20,27,28,29,30,32,39,41,42,43,53,55,64,65,68,69,70,76,77,78,79,80,81,96,101,105,106,107,108,109,110,111,112,115,116,117,118,119,],[-35,-1,-2,-3,-4,-5,-6,-7,-29,-43,-34,-58,-36,48,-40,-42,-57,-25,-27,-30,-31,-8,-9,-53,-54,-21,-39,-41,-26,-28,-37,-32,-38,-33,-20,-24,-49,-50,-47,-48,-51,-52,-22,-23,-55,-44,-45,-46,-56,]),'COMA':([4,5,6,7,8,9,10,11,12,14,19,20,27,28,29,30,32,35,36,37,38,39,41,42,43,50,51,52,53,55,64,65,68,69,70,74,75,76,77,78,79,80,81,96,101,105,106,107,108,109,110,111,112,115,116,117,118,119,],[-35,-1,-2,-3,-4,-5,-6,-7,-29,-43,-34,-58,-36,49,-40,-42,-57,54,56,-11,-13,-25,-27,-30,-31,71,72,73,-8,-9,-53,-54,-21,-39,-41,-10,-12,-26,-28,-37,-32,-38,-33,-20,-24,-49,-50,-47,-48,-51,-52,-22,-23,-55,-44,-45,-46,-56,]),'EXCLAMACION':([4,12,19,27,39,41,42,43,64,76,77,78,79,80,81,102,],[-35,-29,-34,-36,-25,-27,-30,-31,84,-26,-28,-37,-32,-38,-33,84,]),'MAYORQUE':([4,12,19,27,39,41,42,43,64,76,77,78,79,80,81,102,],[-35,-29,-34,-36,-25,-27,-30,-31,85,-26,-28,-37,-32,-38,-33,85,]),'MENORQUE':([4,12,19,27,39,41,42,43,64,76,77,78,79,80,81,102,],[-35,-29,-34,-36,-25,-27,-30,-31,86,-26,-28,-37,-32,-38,-33,86,]),'OPERADORLOGICO':([4,12,19,27,39,41,42,43,65,68,76,77,78,79,80,81,96,101,103,104,111,112,],[-35,-29,-34,-36,-25,-27,-30,-31,87,-21,-26,-28,-37,-32,-38,-33,-20,87,87,87,-22,-23,]),'ELSE':([4,12,19,27,39,41,42,43,68,76,77,78,79,80,81,96,101,103,104,111,112,],[-35,-29,-34,-36,-25,-27,-30,-31,-21,-26,-28,-37,-32,-38,-33,-20,-24,113,114,-22,-23,]),'CERRARPARENTESIS':([4,19,27,42,43,53,55,58,59,60,61,62,63,78,79,80,81,90,91,92,93,94,95,],[-35,-34,-36,-30,-31,-8,-9,76,77,78,79,80,81,-37,-32,-38,-33,105,106,107,108,109,110,]),'CERRARCORCHETE':([35,36,37,38,74,75,],[53,55,-11,-13,-10,-12,]),'INT':([48,],[66,]),'STR':([48,],[67,]),'BOOLEANO':([48,87,88,89,97,98,],[68,68,68,68,111,112,]),'IF':([66,67,],[88,89,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignVariable':([0,14,49,],[1,30,70,]),'expr':([3,13,48,82,87,88,89,],[5,25,64,96,102,102,102,]),'lambda':([3,31,33,34,],[7,50,51,52,]),'filter':([3,],[8,]),'map':([3,],[9,]),'reduce':([3,],[10,]),'lista':([3,71,72,73,],[11,91,93,95,]),'term':([3,13,21,22,23,24,40,44,45,46,47,48,82,87,88,89,],[12,26,39,41,42,43,57,58,59,60,62,12,12,12,12,12,]),'parametros':([14,],[28,]),'lisString':([18,],[35,]),'lisInt':([18,],[36,]),'evaluarCondicion':([48,87,88,89,],[65,101,103,104,]),'condicion':([64,102,],[82,82,]),'cualquierCosa':([113,114,],[115,119,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assignVariable","S'",1,None,None,None),
  ('assignVariable -> VARIABLE IGUAL expr','assignVariable',3,'p_assignVariable','Parser.py',7),
  ('assignVariable -> VARIABLE IGUAL STRING','assignVariable',3,'p_assignVariable','Parser.py',8),
  ('assignVariable -> VARIABLE IGUAL lambda','assignVariable',3,'p_assignVariable','Parser.py',9),
  ('assignVariable -> VARIABLE IGUAL filter','assignVariable',3,'p_assignVariable','Parser.py',10),
  ('assignVariable -> VARIABLE IGUAL map','assignVariable',3,'p_assignVariable','Parser.py',11),
  ('assignVariable -> VARIABLE IGUAL reduce','assignVariable',3,'p_assignVariable','Parser.py',12),
  ('assignVariable -> VARIABLE IGUAL lista','assignVariable',3,'p_assignVariable','Parser.py',13),
  ('lista -> ABRIRCORCHETE lisString CERRARCORCHETE','lista',3,'p_lista','Parser.py',17),
  ('lista -> ABRIRCORCHETE lisInt CERRARCORCHETE','lista',3,'p_lista','Parser.py',18),
  ('lisString -> lisString COMA STRING','lisString',3,'p_lisString','Parser.py',22),
  ('lisString -> STRING','lisString',1,'p_lisString','Parser.py',23),
  ('lisInt -> lisInt COMA NUMERO','lisInt',3,'p_lisInt','Parser.py',27),
  ('lisInt -> NUMERO','lisInt',1,'p_lisInt','Parser.py',28),
  ('condicion -> IGUAL IGUAL','condicion',2,'p_condicion','Parser.py',36),
  ('condicion -> EXCLAMACION IGUAL','condicion',2,'p_condicion','Parser.py',37),
  ('condicion -> MAYORQUE IGUAL','condicion',2,'p_condicion','Parser.py',38),
  ('condicion -> MENORQUE IGUAL','condicion',2,'p_condicion','Parser.py',39),
  ('condicion -> MAYORQUE','condicion',1,'p_condicion','Parser.py',40),
  ('condicion -> MENORQUE','condicion',1,'p_condicion','Parser.py',41),
  ('evaluarCondicion -> expr condicion expr','evaluarCondicion',3,'p_evaluarCondicion','Parser.py',45),
  ('evaluarCondicion -> BOOLEANO','evaluarCondicion',1,'p_evaluarCondicion','Parser.py',46),
  ('evaluarCondicion -> expr IGUAL IGUAL BOOLEANO','evaluarCondicion',4,'p_evaluarCondicion','Parser.py',47),
  ('evaluarCondicion -> expr EXCLAMACION IGUAL BOOLEANO','evaluarCondicion',4,'p_evaluarCondicion','Parser.py',48),
  ('evaluarCondicion -> evaluarCondicion OPERADORLOGICO evaluarCondicion','evaluarCondicion',3,'p_evaluarCondicion','Parser.py',49),
  ('expr -> expr MAS term','expr',3,'p_expr','Parser.py',53),
  ('expr -> ABRIRPARENTESIS expr MAS term CERRARPARENTESIS','expr',5,'p_expr','Parser.py',54),
  ('expr -> expr MENOS term','expr',3,'p_expr','Parser.py',55),
  ('expr -> ABRIRPARENTESIS expr MENOS term CERRARPARENTESIS','expr',5,'p_expr','Parser.py',56),
  ('expr -> term','expr',1,'p_expr','Parser.py',57),
  ('term -> term POR term','term',3,'p_term','Parser.py',61),
  ('term -> term DIVIDIR term','term',3,'p_term','Parser.py',62),
  ('term -> ABRIRPARENTESIS term POR NUMERO CERRARPARENTESIS','term',5,'p_term','Parser.py',63),
  ('term -> ABRIRPARENTESIS term DIVIDIR NUMERO CERRARPARENTESIS','term',5,'p_term','Parser.py',64),
  ('term -> NUMERO','term',1,'p_term','Parser.py',65),
  ('term -> VARIABLE','term',1,'p_term','Parser.py',66),
  ('term -> STRING','term',1,'p_term','Parser.py',67),
  ('term -> ABRIRPARENTESIS term POR term CERRARPARENTESIS','term',5,'p_term','Parser.py',68),
  ('term -> ABRIRPARENTESIS term DIVIDIR term CERRARPARENTESIS','term',5,'p_term','Parser.py',69),
  ('parametros -> parametros COMA VARIABLE','parametros',3,'p_parametros','Parser.py',73),
  ('parametros -> VARIABLE','parametros',1,'p_parametros','Parser.py',74),
  ('parametros -> parametros COMA assignVariable','parametros',3,'p_parametros','Parser.py',75),
  ('parametros -> assignVariable','parametros',1,'p_parametros','Parser.py',76),
  ('parametros -> <empty>','parametros',0,'p_parametros','Parser.py',77),
  ('cualquierCosa -> STRING','cualquierCosa',1,'p_cualquierCosa','Parser.py',81),
  ('cualquierCosa -> NUMERO','cualquierCosa',1,'p_cualquierCosa','Parser.py',82),
  ('cualquierCosa -> VARIABLE','cualquierCosa',1,'p_cualquierCosa','Parser.py',83),
  ('map -> MAPA ABRIRPARENTESIS lambda COMA VARIABLE CERRARPARENTESIS','map',6,'p_map','Parser.py',87),
  ('map -> MAPA ABRIRPARENTESIS lambda COMA lista CERRARPARENTESIS','map',6,'p_map','Parser.py',88),
  ('filter -> FILTER ABRIRPARENTESIS lambda COMA VARIABLE CERRARPARENTESIS','filter',6,'p_filter','Parser.py',92),
  ('filter -> FILTER ABRIRPARENTESIS lambda COMA lista CERRARPARENTESIS','filter',6,'p_filter','Parser.py',93),
  ('reduce -> REDUCE ABRIRPARENTESIS lambda COMA VARIABLE CERRARPARENTESIS','reduce',6,'p_reduce','Parser.py',97),
  ('reduce -> REDUCE ABRIRPARENTESIS lambda COMA lista CERRARPARENTESIS','reduce',6,'p_reduce','Parser.py',98),
  ('lambda -> LAMBDA parametros DOSPUNTOS expr','lambda',4,'p_lambda','Parser.py',102),
  ('lambda -> LAMBDA parametros DOSPUNTOS evaluarCondicion','lambda',4,'p_lambda','Parser.py',103),
  ('lambda -> LAMBDA parametros DOSPUNTOS INT IF evaluarCondicion ELSE cualquierCosa','lambda',8,'p_lambda','Parser.py',104),
  ('lambda -> LAMBDA parametros DOSPUNTOS STR IF evaluarCondicion ELSE cualquierCosa','lambda',8,'p_lambda','Parser.py',105),
  ('filter -> FILTER error','filter',2,'p_filter_error','Parser.py',109),
  ('assignVariable -> VARIABLE IGUAL expr error','assignVariable',4,'p_assignVariable_error','Parser.py',114),
]
