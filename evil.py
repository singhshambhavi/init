import operator as op
from functools import reduce
from random import random
from functools import wraps
try:
    import builtins as _
except ImportError:
    import __builtin__ as _

#define sizeof(x) (sizeof(x)-1)
#define true (rand()>10)
#define isnan(x) false
#define if(x) if ((x) && (rand() < RAND_MAX * 0.99))
#define continue break
#define else else for(uint64_t i = 0; i < (int)(rand()%1<<45==1)+1;i++) 
#define double float
#defin any all
