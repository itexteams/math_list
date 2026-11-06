import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang3_p2_b1_c3_hh10(self):
            # Khai báo biến
            x=symbols('x')
            y=symbols('y')
            a1=randint(-9,9)
            b1=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])

            t=randint(1,9)

            xa=randint(-9,9)
            ya=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])

            xm=randint(-9,9)
            ym=randint(-9,9)

            while a1==0 or a1==b1 or ya==0 or a1/b1==xa/ya :
                x=symbols('x')
                y=symbols('y')
                a1=randint(-9,9)
                b1=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])

                t=randint(1,9)

                xa=randint(-9,9)
                ya=random.choice([1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6,-7,-8,-9])

                xm=randint(-9,9)
                ym=randint(-9,9)



            dtm1=-b1*x+a1*y+b1*xa-a1*ya
            # Tìm ước chung lớn nhất (GCD) của các hệ số
            gcd = math.gcd(math.gcd(-b1,a1),(b1*xa-a1*ya))
            # Rút gọn các hệ số
            hs_a1 = -b1// gcd
            hs_b1 = a1 // gcd
            hs_c1 = (b1*xa-a1*ya) // gcd
            #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            dtm = hs_a1*x+hs_b1*y+hs_c1

            xb=xa+a1*t
            yb=ya+b1*t
            qd=sqrt((xb-xa)**2+(yb-ya)**2)
            qds=sqrt((xb-xa)**2+(yb-ya)**2+1)
            # Nội dung câu hỏi
            noidungcauhoi = ('Chuyển động của vật thể $M$ được thể hiện trên mặt phẳng tọa độ $(Oxy)$. Vật thể $M$ khởi hành từ điểm $A(%s;%s)$ và chuyển động thẳng đều với vectơ vận tốc là $\\vec{v}=(%s;%s)$'
                            %(latex(xa),latex(ya),latex(a1),latex(b1),))



            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Vectơ chỉ phương của đường thẳng biểu diễn chuyển động của vật thể là $\\vec{v}=(%s;%s)$'%(latex(a1),latex(b1))
            nb_da_1_s = 'Vectơ chỉ phương của đường thẳng biểu diễn chuyển động của vật thể là $\\vec{v}=(%s;%s)$'%(latex(b1),latex(a1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Vectơ chỉ phương của đường thẳng biểu diễn chuyển động của vật thể là $\\vec{v}=(%s;%s)$'%(latex(a1),latex(b1))
            nb_da_2_s = 'Vectơ chỉ phương của đường thẳng biểu diễn chuyển động của vật thể là $\\vec{v}=(%s;%s)$'%(latex(b1),latex(a1))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]

            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Vectơ chỉ phương của đường thẳng biểu diễn chuyển động của vật thể là $\\vec{v}=(%s;%s)$.'
                            %(latex(a1),latex(b1))
                        )
            loigiai_nb_2 = ('Vectơ chỉ phương của đường thẳng biểu diễn chuyển động của vật thể là $\\vec{v}=(%s;%s)$.'
                            %(latex(a1),latex(b1))
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Vật thể $M$ chuyển động trên đường thẳng $%s=0$'%(latex(dtm))
            th_da_1_s = 'Vật thể $M$ chuyển động trên đường thẳng $%s=0$'%(latex(dtm+1))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True Vật thể $M$ chuyển động trên đường thẳng $%s=0$'%(latex(dtm))
            th_da_2_s = 'Vật thể $M$ chuyển động trên đường thẳng $%s=0$'%(latex(dtm-1))
            list_th_da_2=[th_da_2_d,th_da_2_s]

            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Vectơ chỉ phương của đường thẳng biểu diễn chuyển động của vật thể $M$ là $\\vec{v}=(%s;%s)$, do đó đường thẳng này có vectơ pháp tuyến là $\\vec{n}=(%s;%s)$.'
                            ' Mặt khác đường thằng này đi qua điểm $A(%s;%s)$ nên có phương trình $%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0$.'
                            %(latex(a1),latex(b1),latex(-b1),latex(a1),latex(xa),latex(ya), latex(-b1),latex(xa),latex(a1),latex(ya),latex(dtm),)
                        )
            loigiai_th_2 =  ('Vectơ chỉ phương của đường thẳng biểu diễn chuyển động của vật thể $M$ là $\\vec{v}=(%s;%s)$, do đó đường thẳng này có vectơ pháp tuyến là $\\vec{n}=(%s;%s)$.'
                            ' Mặt khác đường thằng này đi qua điểm $A(%s;%s)$ nên có phương trình $%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0$.'
                            %(latex(a1),latex(b1),latex(-b1),latex(a1),latex(xa),latex(ya), latex(-b1),latex(xa),latex(a1),latex(ya),latex(dtm),)
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Tọa độ của điểm $M$ tại thời điểm $t$ $(t>0)$ tính từ khi khởi hành là $(%s+%s t;%s+%s t)$'%(latex(xa),latex(a1),latex(ya),latex(b1),)
            vd_da_1_s = 'Tọa độ của điểm $M$ tại thời điểm $t$ $(t>0)$ tính từ khi khởi hành là $(%s+%s t;%s+%s t)$'%(latex(a1),latex(xa),latex(b1),latex(ya),)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Tọa độ của điểm $M$ tại thời điểm $t$ $(t>0)$ tính từ khi khởi hành là $(%s+%s t;%s+%s t)$'%(latex(xa),latex(a1),latex(ya),latex(b1),)
            vd_da_2_s = 'Tọa độ của điểm $M$ tại thời điểm $t$ $(t>0)$ tính từ khi khởi hành là $(%s+%s t;%s+%s t)$'%(latex(a1),latex(xa),latex(b1),latex(ya),)
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]

            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('Vật thể khởi hành từ điểm $A(%s;%s)$ chuyển thẳng đều với vận tốc là $\\vec{v}=(%s;%s)$ nên vị trí của vật thể tại thời điểm $t (t>0)$ có tọa độ $(%s+%s t;%s+%s t)$.'

                            %(latex(xa),latex(ya),latex(a1),latex(b1), latex(xa),latex(a1),latex(ya),latex(b1),)

                        )
            loigiai_vd_2 = ('Vật thể khởi hành từ điểm $A(%s;%s)$ chuyển thẳng đều với vận tốc là $\\vec{v}=(%s;%s)$ nên vị trí của vật thể tại thời điểm $t (t>0)$ có tọa độ $(%s+%s t;%s+%s t)$.'

                            %(latex(xa),latex(ya),latex(a1),latex(b1), latex(xa),latex(a1),latex(ya),latex(b1),)

                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Khi $t=%s$ thì vật thể $M$ chuyển động được quãng đường độ dài bằng $%s$'%(latex(t),latex(qd))
            vdc_da_1_s = 'Khi $t=%s$ thì vật thể $M$ chuyển động được quãng đường độ dài bằng $%s$'%(latex(t),latex(qds))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Khi $t=%s$ thì vật thể $M$ chuyển động được quãng đường độ dài bằng $%s$'%(latex(t),latex(qd))
            vdc_da_2_s = 'Điểm Khi $t=%s$ thì vật thể $M$ chuyển động được quãng đường độ dài bằng $%s$'%(latex(t),latex(qds))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Gọi $B$ là vị trí vật thể tại thời điểm $t=%s$. Do đó, tọa độ điểm $B$ là\\\\ \n'
                            ' $(%s+%s \\cdot (%s);%s+%s\\cdot (%s))=(%s;%s)$.\\\\ \n'
                            'Ta có $\\vec{AB}=(%s;%s)$. Quãng đường vật thể đi được là $AB=\\sqrt{(%s)^2+(%s)^2}=%s$.'
                            %(latex(t),latex(xa),latex(a1),latex(t),latex(ya),latex(b1),latex(t),latex(xb),latex(yb),
                            latex(xb-xa),latex(yb-ya),latex(xb-xa),latex(yb-ya),latex(qd))
                        )
            loigiai_vdc_2 = ('Gọi $B$ là vị trí vật thể tại thời điểm $t=%s$. Do đó, tọa độ điểm $B$ là\\\\ \n'
                            ' $(%s+%s \\cdot (%s);%s+%s\\cdot (%s))=(%s;%s)$.\\\\ \n'
                            'Ta có $\\vec{AB}=(%s;%s)$. Quãng đường vật thể đi được là $AB=\\sqrt{(%s)^2+(%s)^2}=%s$.'
                            %(latex(t),latex(xa),latex(a1),latex(t),latex(ya),latex(b1),latex(t),latex(xb),latex(yb),
                            latex(xb-xa),latex(yb-ya),latex(xb-xa),latex(yb-ya),latex(qd))
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('++','+').replace('--','+').replace('+-','-').replace('-+','-')
            return content   

