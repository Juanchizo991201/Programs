# 
# UNIVERSIDAD SERGIO ARBOLEDA
# ESCUELA DE CIENCIAS EXACTAS E INGENIERÍA
# INGENIERÍA DE SISTEMAS Y TELECOMUNICACIONES
# 
# AUTHORS: JUAN JOSÉ MONTENEGRO PULIDO & CAMILO ANDRÉS ROMERO MALDONADO
# EMAILS: juan.montenegro@correo.usa.edu.co & camiloa.romero@correo.usa.edu.co
# 
# 12/03/2021
# 

COMPILER = gcc
FLAGS = -pedantic -Wall -fopenmp
OBJ = -c

CONVENTIONAL = MM1c
TRANSPOSE = MM1f
CLASSICDYNAMIC = MM1cDynamic
TRANSPOSEDYNAMIC = MM1fDynamic

PROGS = $(CONVENTIONAL) $(TRANSPOSE) $(CLASSICDYNAMIC) $(TRANSPOSEDYNAMIC)

all: $(PROGS)

$(CONVENTIONAL):
		$(COMPILER) $(FLAGS) $(OBJ) matrix.c
		$(COMPILER) $(FLAGS) $(OBJ) $@.c
		$(COMPILER) $(FLAGS) -o $@ $@.o matrix.o 
		
$(TRANSPOSE):
		$(COMPILER) $(FLAGS) $(OBJ) matrix.c
		$(COMPILER) $(FLAGS) $(OBJ) $@.c
		$(COMPILER) $(FLAGS) -o $@ $@.o matrix.o 

$(CLASSICDYNAMIC):
		$(COMPILER) $(FLAGS) $(OBJ) matrix.c
		$(COMPILER) $(FLAGS) $(OBJ) $@.c
		$(COMPILER) $(FLAGS) -o $@ $@.o matrix.o 

$(TRANSPOSEDYNAMIC):
		$(COMPILER) $(FLAGS) $(OBJ) matrix.c
		$(COMPILER) $(FLAGS) $(OBJ) $@.c
		$(COMPILER) $(FLAGS) -o $@ $@.o matrix.o 

clean:
		$(RM) $(PROGS) *.o