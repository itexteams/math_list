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


def bt_dang7_p2_b2_c3_ds12(self):
            # Khai báo biến
            t=symbols('t')
            k=randint(1,5)
            t0=4*k
            t4=8*k

            a=-1 
            b=t0+t4
            c=-t0*t4

            y=-t**2+(t0+t4)*t-t0*t4
            t3=Rational(t0+t4,2)
            y3=-t3**2+(t0+t4)*t3-t0*t4
            t2=Rational(t0,2)
            t1=Rational(t0+t3,2)
            yt2=-t1**2+(t0+t4)*t1-t0*t4

            s1=Rational(t2*yt2,2)
            s2=(t1-t2)*yt2
            dh=-Rational(1,3)*t**3+Rational(t0+t4,2)*t**2-t0*t4*t
            dh4=-Rational(1,3)*t4**3+Rational(t0+t4,2)*t4**2-t0*t4*t4
            dh1=-Rational(1,3)*t1**3+Rational(t0+t4,2)*t1**2-t0*t4*t1
            s3=dh4-dh1
            kq=s1+s2+s3
            # Nội dung câu hỏi
            noidungcauhoi = ('''\\immini{Một chất điểm chuyển động thẳng trong $%s$ giây với vận tốc $v(t)$ (đơn vị: m/s) là hàm số phụ thuộc thời gian $t$ (đơn vị: giây) có đồ thị như hình vẽ.}
                            {\\scalebox{0.6}{ 
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                \\draw[->] (-1,0) -- (9,0) node[below] {$t$};
                \\draw[->] (0,-1) -- (0,5) node[left] {$v(t)$};
                \\draw[thick, red] (0,0) -- (2,3);
                \\draw[thick, red] (2,3) -- (5,3);
                \\draw[dashed] (2,0) -- (2,3);
                \\draw[dashed] (0,3) -- (2,3);
                \\draw[dashed] (0,4) -- (6,4);
                \\draw[dashed] (5,0) -- (5,3);
                \\draw[domain=5:8, smooth, variable=\\x, red, thick]
                plot ({\\x}, {-(\\x - 6)^2 + 4});
                \\draw (0,0) node[below left] {$O$};
                \\draw (2,0) node[below] {$%s$};
                \\draw (5,0) node[below] {$%s$};
                \\draw (6,0) node[below] {$%s$};
                \\draw (8,0) node[below] {$%s$};
                \\draw (0,3) node[left] {$%s$};
                \\draw (0,4) node[left] {$%s$};
                \\draw (1.5,1) node[left] {$S_1$};
                \\draw (3.5,1.5) node[left] {$S_2$};
                \\draw (6,2) node[left] {$S_3$};
            \\end{tikzpicture}}}'''                 
                            %(latex(t4),
                            latex(t2),latex(t1),latex(t3),latex(t4),latex(yt2),latex(y3)
                                ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Tại thời điểm $t=%s$ giây, vận tốc của chất điểm bằng $0$ m/s' %(latex(t4))
            nb_da_1_s = 'Tại thời điểm $t=%s$ giây, vận tốc của chất điểm bằng $%s$ m/s' %(latex(t4),latex(y3))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Quan sát đồ thị của hàm số vận tốc theo $t$, tại thời điểm $t=%s$ giây ta thấy vận tốc của chất điểm bằng $0$ m/s.'''
                        %(latex(t4)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Quãng đường chất điểm đi được trong khoảng thời gian từ $0$ giây đến $%s$ giây bằng $%s$ m' %(latex(t2),latex(Rational(t2*yt2,2)))  
            th_da_1_s = 'Quãng đường chất điểm đi được trong khoảng thời gian từ $0$ giây đến $%s$ giây bằng $%s$ m' %(latex(t2),latex(1+Rational(t2*yt2,2)))  
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Quãng đường chất điểm đi được trong khoảng thời gian từ $0$ giây đến $%s$ giây bằng diện tích tam giác vuông $S_1$. \\\\
                            Ta có $S_1=\\frac{1}{2} \\cdot %s \\cdot %s=%s$ m.'''       
                        %(latex(t2),latex(t2),latex(yt2),latex(Rational(t2*yt2,2))
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Trong khoảng thời gian từ $%s$ giây đến $%s$ giây đồ thị $v(t)$ là một phần của đường parabol $y=ax^2+bx+c$. Khi đó $v(t)=%s$' %(latex(t1),latex(t4),latex(y))  
            vd_da_1_s = 'Trong khoảng thời gian từ $%s$ giây đến $%s$ giây đồ thị $v(t)$ là một phần của đường parabol $y=ax^2+bx+c$. Khi đó $v(t)=%s$' %(latex(t1),latex(t4),latex(y+1)) 
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Trong khoảng thời gian từ $%s$ giây đến $%s$ giây đồ thị $v(t)$ là một phần của đường parabol $y=ax^2+bx+c$. Parabol đi qua các điểm $(%s;%s), (%s;%s), (%s;0)$.\\\\
                            Ta có hệ phương trình $\\heva{& %s a+%s b+c=%s \\\\& %s a+%s b+c=%s \\\\& %s a+%s b+c=0 } \\Leftrightarrow \\heva{& a=%s \\\\& b=%s \\\\& c=%s}$. \\\\
                                Vậy $v(t)=%s$.'''  
                        %(latex(t1),latex(t4),
                        latex(t1),latex(yt2),latex(t3),latex(y3),latex(t4),
                        latex(t1**2),latex(t1),latex(yt2),
                        latex(t3**2),latex(t3),latex(y3),
                        latex(t4**2),latex(t4),
                        latex(a),latex(b),latex(c),
                        latex(y)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Quãng đường chất điểm đi được từ lúc xuất phát đến khi dừng lại bằng $%s$ m' %(latex(kq)) 
            vdc_da_1_s = 'Quãng đường chất điểm đi được từ lúc xuất phát đến khi dừng lại bằng $%s$ m' %(latex(kq+1)) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Quãng đường chất điểm đi được từ lúc xuất phát đến khi dừng lại bằng \\\\
                            $S=S_1+S_2+S_3=%s+%s(%s-%s)+\\int \\limits_{%s}^{%s} (%s) \\text{d}t=%s$ m.'''
                        %(latex(Rational(t2*yt2,2)),latex(yt2),latex(t1),latex(t2),
                        latex(t1),latex(t4),latex(y),latex(kq)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

