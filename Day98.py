# Memory Efficiency

import sys
lst=[i for i in range(1,1000001)]
gen=(i for i in range(1,1000001))
print("List size:",sys.getsizeof(lst),"bytes")
print("Generator size:",sys.getsizeof(gen),"bytes")