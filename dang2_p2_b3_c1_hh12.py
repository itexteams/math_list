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


def bt_dang2_p2_b3_c1_hh12(self):
            # Khai báo biến
            x1=randint(-10,10)
            y1=randint(-10,10)
            z1=randint(-10,10)
            x2=randint(-10,10)
            y2=randint(-10,10)
            z2=randint(-10,10)
            l=randint(-5,5)
            t=randint(-5,5)
            d1=(x2-x1)**2+(y2-y1)**2+(z2-z1)**2
            x3=x1+(x2-x1)*t
            y3=y1+(y2-y1)*t
            z3=z1+(z2-z1)*t
            m=randint(-9,9)
            x7=x2+(x2-x1)*m
            while m==0 or m==-1 or l==0 or t==0 or t==1 or x1**2+y1**2+z1**2==0 or x2**2+y2**2+z2**2==0 or x1==x2 or y1==y2 or z1==z2 or d1-y1**2-z1**2<=0 or d1-x1**2-z1**2<=0 or d1-x1**2-y1**2<=0 or x3-x1==0 or y3-y1==0 :   
                x1=randint(-10,10)
                y1=randint(-10,10)
                z1=randint(-10,10)
                x2=randint(-10,10)
                y2=randint(-10,10)
                z2=randint(-10,10)
                l=randint(-5,5)
                t=randint(-5,5)
                d1=(x2-x1)**2+(y2-y1)**2+(z2-z1)**2
                x3=x1+(x2-x1)*t #tọa độ điểm thẳng hàng với A, B
                y3=y1+(y2-y1)*t
                z3=z1+(z2-z1)*t
                m=randint(-9,9)
                x7=x2+(x2-x1)*m
            x4=x1+(x2-x1)*t # tọa độ điểm không thẳng hàng A, B
            y4=y1+(y2-y1)*t
            z4=z1+(z2-z1)*(t+2)
            x5=2*x2-x1+(y2-y1)*l #tọa độ điểm để tìm hình chiếu H
            y5=2*y2-y1-(x2-x1)*l
            z5=2*z2-z1
            dab=nsimplify(d1**(1/2))
            ds1=nsimplify((x2**2+y2**2+z2**2-x1**2-y1**2-z1**2)/(2*x2-2*x1))
            ds2=nsimplify((x2**2+y2**2+z2**2-x1**2-y1**2-z1**2)/(2*y2-2*y1))
            ds3=nsimplify((x2**2+y2**2+z2**2-x1**2-y1**2-z1**2)/(2*z2-2*z1))
            td=(x2-x1)*(-x5)+(y2-y1)*(-y5)+(z2-z1)*(-z5) #hệ số tự do trong tích vô hướng
            k=-nsimplify((x1*(x2-x1)+y1*(y2-y1)+z1*(z2-z1)+td)/d1) # số k trong hai vec to cùng phương
            x6=x1+(x2-x1)*k #tọa độ hình chiếu H
            y6=y1+(y2-y1)*k
            z6=z1+(z2-z1)*k
            y7=nsimplify(y1+((x7-x1)/(x2-x1))*(y2-y1))
            z7=nsimplify(z1+((x7-x1)/(x2-x1))*(z2-z1))
            vd=y7-z7
            # Nội dung câu hỏi
            noidungcauhoi = '''Trong không gian $Oxyz$ cho hai điểm $A(%s;%s;%s)$ và $B(%s;%s;%s)$'''%(latex(x1),latex(y1),latex(z1),latex(x2),latex(y2),latex(z2))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $\\vec{AB}=(%s;%s;%s)$'%(latex(x2-x1),latex(y2-y1),latex(z2-z1))
            nb_da_1_s = ' $\\vec{AB}=(%s;%s;%s)$'%(latex(-x2+x1),latex(-y2+y1),latex(-z2+z1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True $\\vec{BA}=(%s;%s;%s)$'%(latex(-x2+x1),latex(-y2+y1),latex(-z2+z1))
            nb_da_2_s = '$\\vec{BA}=(%s;%s;%s)$'%(latex(x2-x1),latex(y2-y1),latex(z2-z1))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            nb_da_3_d = '\\True $\\vec{AB}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(x2-x1),latex(y2-y1),latex(z2-z1))
            nb_da_3_s = '$\\vec{AB}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(-x2+x1),latex(-y2+y1),latex(-z2+z1))
            list_nb_da_3=[nb_da_3_d,nb_da_3_s]
            nb_da_3=random.choice(list_nb_da_3)

            nb_da_4_d = '\\True $\\vec{BA}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(-x2+x1),latex(-y2+y1),latex(-z2+z1))
            nb_da_4_s = '$\\vec{BA}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(x2-x1),latex(y2-y1),latex(z2-z1))
            list_nb_da_4=[nb_da_4_d,nb_da_4_s]
            nb_da_4=random.choice(list_nb_da_4)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2, nb_da_3, nb_da_4]

            # Nội dung lời giải
            loigiai_nb_1 = ('''$\\vec{AB}=(%s;%s;%s)$.'''%(latex(x2-x1),latex(y2-y1),latex(z2-z1))
                        )
            loigiai_nb_2 = ('''$\\vec{BA}=(%s;%s;%s)$.'''%(latex(-x2+x1),latex(-y2+y1),latex(-z2+z1))
                            )
            loigiai_nb_3 = ('''$\\vec{AB}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$.'''%(latex(x2-x1),latex(y2-y1),latex(z2-z1))
                            )
            loigiai_nb_4 = ('''$\\vec{BA}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$.'''%(latex(-x2+x1),latex(-y2+y1),latex(-z2+z1))
                            )
            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2, loigiai_nb_3,loigiai_nb_4]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d ='\\True $\\abs{\\vec{AB}}=%s$'%(latex(dab))
            th_da_1_s = '$\\abs{\\vec{AB}}=%s$'%(latex(dab+1))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True Trung điểm $M$ của đoạn thẳng $AB$ có tọa độ là $\\left(%s;%s;%s\\right)$'%(latex(nsimplify((x1+x2)/2)),latex(nsimplify((y1+y2)/2)),latex(nsimplify((z1+z2)/2)))
            th_da_2_s = 'Trung điểm $M$ của đoạn thẳng $AB$ có tọa độ là $\\left(%s;%s;%s\\right)$'%(latex(nsimplify((x1+x2)/2)),latex(nsimplify((y1+y2)/2)),latex(nsimplify((z1+z2+2)/2)))
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 =  ('''Ta có $\\vec{AB}=\\left(%s;%s;%s\\right)$, suy ra $\\abs{\\vec{AB}}=%s$.'''%(latex(x2-x1),latex(y2-y1),latex(z2-z1),latex(dab))
                        )
            loigiai_th_2 =  ('''Vì $M$ là trung điểm của đoạn thẳng $AB$ nên tọa độ của điểm $M$ là $\\left(\\dfrac{%s+%s}{2};\\dfrac{%s+%s}{2};\\dfrac{%s+%s}{2}\\right)$, suy ra $M\\left(%s;%s;%s\\right)$.'''%(latex(x1),latex(x2),latex(y1),latex(y2),latex(z1),latex(z2),latex(nsimplify((x1+x2)/2)),latex(nsimplify((y1+y2)/2)),latex(nsimplify((z1+z2)/2)))
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
            vd_da_1_d = '\\True Ba điểm $A$, $B$ và $C(%s;%s;%s)$ thẳng hàng'%(latex(x3),latex(y3),latex(z3))
            vd_da_1_s = 'Ba điểm $A$, $B$ và $C(%s;%s;%s)$ không thẳng hàng'%(latex(x3),latex(y3),latex(z3))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Ba điểm $A$, $B$ và $C(%s;%s;%s)$ không thẳng hàng'%(latex(x4),latex(y4),latex(z4))
            vd_da_2_s = 'Ba điểm $A$, $B$ và $C(%s;%s;%s)$ thẳng hàng'%(latex(x4),latex(y4),latex(z4))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            vd_da_3_d = '\\True Nếu ba điểm $A,B$ và $E(%s;y;z)$ thẳng hàng thì $y-z=%s$'%(latex(x7),latex(vd))
            vd_da_3_s = 'Nếu ba điểm $A,B$ và $E(%s;y;z)$ thẳng hàng thì $y-z=%s$'%(latex(x7),latex(-vd))
            list_vd_da_3=[vd_da_3_d,vd_da_3_s]
            vd_da_3=random.choice(list_vd_da_3)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1,vd_da_2,vd_da_3]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Ta có $\\vec{AB}=\\left(%s;%s;%s\\right)$ và $\\vec{AC}=\\left(%s;%s;%s\\right)$. Vì $\\dfrac{%s}{%s}=\\dfrac{%s}{%s}=\\dfrac{%s}{%s}$ nên hai vectơ $\\vec{AB}$ và $\\vec{AC}$ cùng phương, suy ra ba điểm $A,B,C$ thẳng hàng.'''%(latex(x2-x1),latex(y2-y1),latex(z2-z1),latex(x3-x1),latex(y3-y1),latex(z3-z1),latex(x2-x1),latex(x3-x1),latex(y2-y1),latex(y3-y1),latex(z2-z1),latex(z3-z1))
                            )
            loigiai_vd_2 = ('''Ta có $\\vec{AB}=\\left(%s;%s;%s\\right)$ và $\\vec{AC}=\\left(%s;%s;%s\\right)$. Vì $\\dfrac{%s}{%s} \\neq \\dfrac{%s}{%s}$ nên hai vectơ $\\vec{AB}$ và $\\vec{AC}$ không cùng phương, suy ra ba điểm $A,B,C$ không thẳng hàng.'''%(latex(x2-x1),latex(y2-y1),latex(z2-z1),latex(x4-x1),latex(y4-y1),latex(z4-z1),latex(x2-x1),latex(x4-x1),latex(y4-y1),latex(y4-y1))
                            )
            loigiai_vd_3 = ('''Ta có $\\vec{AB}=\\left(%s;%s;%s\\right)$ và $\\vec{AE}=\\left(%s;y-%s;z-%s\\right)$. \\\\ \n'''
                            'Vì ba điểm $A,B$ và $E$ thẳng hàng nên \\\\ \n'
                            '\\hspace*{1cm}$\\vec{AE}=k\\vec{AB}\\Leftrightarrow \\heva{&%s=%sk\\\\&y-%s=%sk\\\\&z-%s=%sk} \\Leftrightarrow \\heva{&k=%s\\\\&y=%s+%sk\\\\&z=%s+%sk}\\Leftrightarrow \\heva{&k=%s\\\\&y=%s\\\\&z=%s}$.\\\\ \n'
                            'Vậy $y-z=%s-%s=%s$.'

                            %(latex(x2-x1),latex(y2-y1),latex(z2-z1),latex(x7-x1),latex(y1),latex(z1),
                            latex(x7-x1),latex(x2-x1),latex(y1),latex(y2-y1),latex(z1),latex(z2-z1),
                            latex(nsimplify((x7-x1)/(x2-x1))),latex(y1),latex(y2-y1),latex(z1),latex(z2-z1),
                            latex(nsimplify((x7-x1)/(x2-x1))),latex(y7),latex(z7),
                            latex(y7),latex(z7),latex(vd)
                            )
                            )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2,loigiai_vd_3]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Nếu điểm $I(x;y;z)$ thuộc trục $Ox$ và thoả mãn $\\abs{\\vec{AI}}=\\abs{\\vec{BI}}$ thì $x+y+z=%s$'%(latex(ds1))
            vdc_da_1_s = 'Nếu điểm $I(x;y;z)$ thuộc trục $Ox$ và thoả mãn $\\abs{\\vec{AI}}=\\abs{\\vec{BI}}$ thì $x+y+z=%s$'%(latex(ds1+1))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Nếu điểm $I(x;y;z)$ thuộc trục $Oy$ và thoả mãn $\\abs{\\vec{AI}}=\\abs{\\vec{BI}}$ thì $x+y+z=%s$'%(latex(ds2))
            vdc_da_2_s = 'Nếu điểm $I(x;y;z)$ thuộc trục $Oy$ và thoả mãn $\\abs{\\vec{AI}}=\\abs{\\vec{BI}}$ thì $x+y+z=%s$'%(latex(ds2+2))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)

            vdc_da_3_d = '\\True Nếu điểm $I(x;y;z)$ thuộc trục $Oz$ và thoả mãn $\\abs{\\vec{AI}}=\\abs{\\vec{BI}}$ thì $x+y+z=%s$'%(latex(ds3))
            vdc_da_3_s = 'Nếu điểm $I(x;y;z)$ thuộc trục $Oz$ và thoả mãn $\\abs{\\vec{AI}}=\\abs{\\vec{BI}}$ thì $x+y+z=%s$'%(latex(ds3-1))
            list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
            vdc_da_3=random.choice(list_vdc_da_3)

            vdc_da_4_d = '\\True Nếu điểm $H(x;y;z)$ là hình chiếu của điểm $D(%s;%s;%s)$ lên đường thẳng $AB$ \\\\ thì $x+y+z=%s$'%(latex(x5),latex(y5),latex(z5),latex(x6+y6+z6))
            vdc_da_4_s = 'Nếu điểm $H(x;y;z)$ là hình chiếu của điểm $D(%s;%s;%s)$ lên đường thẳng $AB$ thì $x+y+z=%s$'%(latex(x5),latex(y5),latex(z5),latex(-x6-y6-z6))
            list_vdc_da_4=[vdc_da_4_d,vdc_da_4_s]
            vdc_da_4=random.choice(list_vdc_da_4)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1,vdc_da_2,vdc_da_3,vdc_da_4]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Vì điểm $I$ thuộc trục $Ox$ nên suy ra $I(x;0;0)$.\\\\ \n'
                            'Ta có $\\vec{AI}=(x-%s;%s;%s)$ và $\\vec{BI}=(x-%s;%s;%s)$ mà $\\abs{\\vec{AI}}=\\abs{\\vec{BI}}$ nên suy ra\\\\ \n'
                            '\\begin{eqnarray*} \n'
                            '\\sqrt{(x-%s)^2+(%s)^2+(%s)^2}&=&\\sqrt{(x-%s)^2+(%s)^2+(%s)^2}\\\\ \n'
                            'x^2-%sx+%s+%s+%s&=&x^2-%sx+%s+%s+%s\\\\ \n'
                            '%sx&=&%s\\\\ \n'
                            'x&=&%s.\\\\ \n'
                            '\\end{eqnarray*}\\\\ \n'
                            'Vậy $x+y+z=%s$.'
                            %(latex(x1),latex(-y1),latex(-z1),latex(x2),latex(-y2),latex(-z2),latex(x1),latex(-y1),latex(-z1),latex(x2),latex(-y2),latex(-z2),
                            latex(2*x1),latex(x1**2),latex(y1**2),latex(z1**2),
                            latex(2*x2),latex(x2**2),latex(y2**2),latex(z2**2),
                            latex(2*(x2-x1)),latex(x2**2+y2**2+z2**2-x1**2-y1**2-z1**2),latex(ds1),latex(ds1))
                        )
            loigiai_vdc_2 = ('Vì điểm $I$ thuộc trục $Oy$ nên suy ra $I(0;y;0)$.\\\\ \n'
                            'Ta có $\\vec{AI}=(%s;y-%s;%s)$ và $\\vec{BI}=(%s;y-%s;%s)$ mà $\\abs{\\vec{AI}}=\\abs{\\vec{BI}}$ nên suy ra\\\\ \n'
                            '\\begin{eqnarray*} \n'
                            '\\sqrt{(%s)^2+(y-%s)^2+(%s)^2}&=&\\sqrt{(%s)^2+(y-%s)^2+(%s)^2}\\\\ \n'
                            '%s+y^2-%sy+%s+%s&=&%s+y^2-%sy+%s+%s\\\\ \n'
                            '%sy&=&%s\\\\ \n'
                            'y&=&%s.\\\\ \n'
                            '\\end{eqnarray*}\\\\ \n'
                            'Vậy $x+y+z=%s$.'
                            %(latex(-x1),latex(y1),latex(-z1),latex(-x2),latex(y2),latex(-z2),latex(-x1),latex(y1),latex(-z1),latex(-x2),latex(y2),latex(-z2),
                            latex(x1**2),latex(2*y1),latex(y1**2),latex(z1**2),
                            latex(x2**2),latex(2*y2),latex(y2**2),latex(z2**2),
                            latex(2*(y2-y1)),latex(x2**2+y2**2+z2**2-x1**2-y1**2-z1**2),latex(ds2),latex(ds2))
                        )
            loigiai_vdc_3 = ('Vì điểm $I$ thuộc trục $Oz$ nên suy ra $I(0;0;z)$.\\\\ \n'
                            'Ta có $\\vec{AI}=(%s;%s;z-%s)$ và $\\vec{BI}=(%s;%s;z-%s)$ mà $\\abs{\\vec{AI}}=\\abs{\\vec{BI}}$ nên suy ra\\\\ \n'
                            '\\begin{eqnarray*} \n'
                            '\\sqrt{(%s)^2+(%s)^2+(z-%s)^2}&=&\\sqrt{(%s)^2+(%s)^2+(z-%s)^2}\\\\ \n'
                            '%s+%s+z^2-%sz+%s&=&%s+%s+z^2-%sz+%s\\\\ \n'
                            '%sz&=&%s\\\\ \n'
                            'z&=&%s.\\\\ \n'
                            '\\end{eqnarray*}\\\\ \n'
                            'Vậy $x+y+z=%s$.'
                            %(latex(-x1),latex(-y1),latex(z1),latex(-x2),latex(-y2),latex(z2),latex(-x1),latex(-y1),latex(z1),latex(-x2),latex(-y2),latex(z2),
                            latex(x1**2),latex(y1**2),latex(2*z1),latex(z1**2),
                            latex(x2**2),latex(y2**2),latex(2*z2),latex(z2**2),
                            latex(2*(z2-z1)),latex(x2**2+y2**2+z2**2-x1**2-y1**2-z1**2),latex(ds3),latex(ds3))
                        )
            loigiai_vdc_4 = ('Theo bài ta có $\\vec{AB}=(%s;%s;%s)$, $\\vec{DH}=(x-%s;y-%s;z-%s)$ và $\\vec{AH}=(x-%s;y-%s;z-%s)$.\\\\ \n'
                            'Vì ba điểm $A ,B, H$ thẳng hàng nên vectơ $\\vec{AH}$ cùng phương với vectơ $\\vec{AB}$ .\\\\ \n'
                            'Ta có \\\\ \n'
                            '\\hspace*{1cm}$\\vec{AH}=k\\vec{AB} \\Leftrightarrow \\heva{&x-%s=%sk\\\\&y-%s=%sk\\\\&z-%s=%sk} \\Leftrightarrow \\heva{&x=%s+%sk\\\\&y=%s+%sk\\\\&z=%s+%sk}$ (1).\\\\ \n'
                            'Vì điểm $H$ là hình chiếu của điểm $D$ lên đường thẳng $AB$ nên $\\vec{AB}\\perp \\vec{DH}$.\\\\ \n'
                            'Suy ra\\\\'
                            '$\\vec{AB}\\cdot\\vec{DH}=0\\Leftrightarrow %s(x-%s)+%s(y-%s)+%s(z-%s)=0\\Leftrightarrow %sx+%sy+%sz+%s=0$. (2)\\\\ \n'
                            'Thế $x,y,z$ ở hệ phương trình (1) vào phương trình (2) ta được \\\\ \n'
                            '\\hspace*{1cm}$%s(%s+%sk)+%s(%s+%sk)+%s(%s+%sk)+%s=0\\Leftrightarrow k=%s$.\\\\ \n'
                            'Thay $k=%s$ vào (1) ta được $\\heva{&x=%s\\\\&y=%s\\\\&z=%s}$.\\\\ \n'
                            'Vậy $x+y+z=%s+%s+%s=%s$.'
                            %(latex(x2-x1),latex(y2-y1),latex(z2-z1),
                            latex(x5),latex(y5),latex(z5),
                            latex(x1),latex(y1),latex(z1),
                            latex(x1),latex(x2-x1),latex(y1),latex(y2-y1),latex(z1),latex(z2-z1),latex(x1),latex(x2-x1),latex(y1),latex(y2-y1),latex(z1),latex(z2-z1),
                            latex(x2-x1),latex(x5),latex(y2-y1),latex(y5),latex(z2-z1),latex(z5),
                            latex(x2-x1),latex(y2-y1),latex(z2-z1),latex(td),
                            latex(x2-x1),latex(x1),latex(x2-x1),latex(y2-y1),latex(y1),latex(y2-y1),latex(z2-z1),latex(z1),latex(z2-z1),latex((x2-x1)*(-x5)+(y2-y1)*(-y5)+(z2-z1)*(-z5)),
                            latex(k),latex(k),latex(x6),latex(y6),latex(z6),latex(x6),latex(y6),latex(z6),latex(x6+y6+z6)
                            )
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2,loigiai_vdc_3,loigiai_vdc_4]

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('1\\vec','\\vec').replace('-1\\vec','-\\vec').replace('+-','-').replace('\\frac','\\dfrac').replace('--','+').replace('-0x','').replace('+0x','').replace('+0','').replace('-0','').replace('=0+','').replace('=0-','-').replace('+1k','+k').replace('-1k','-k').replace('+0k','').replace('-0k','').replace('=1k','=k').replace('=-1k','=-k')
            return content

