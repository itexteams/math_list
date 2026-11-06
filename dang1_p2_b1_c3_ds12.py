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


def bt_dang1_p2_b1_c3_ds12(self):
            # Khai báo biến
            h=randint(1,7)
            a1=randint(1,50)
            a=-a1/10
            b=randint(1,50)
            while (a/4)*(-b/a)**4+(b/3)*(-b/a)**3>130 or a*((-2*b)/(3*a))**3+b*((-2*b)/(3*a))**2<20 or -b/a>14 or -b/a<5:
                h=randint(1,7)
                a1=randint(1,50)
                a=-a1/10
                b=randint(1,50)
            t1=nsimplify(-b/a)
            t2=nsimplify(-2*b/(3*a))
            hmm=nsimplify((a/4)*(-b/a)**4+(b/3)*(-b/a)**3+h)
            h22=nsimplify((a/4)*((-2*b)/(3*a))**4+(b/3)*((-2*b)/(3*a))**3+h)
            vmm=nsimplify((a)*((-2*b)/(3*a))**3+(b)*((-2*b)/(3*a))**2)
            number = Decimal(float(hmm))  # Số cần làm tròn
            hm = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            number = Decimal(float(h22))  # Số cần làm tròn
            h2 = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            number = Decimal(float(vmm))  # Số cần làm tròn
            vm = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            # Nội dung câu hỏi
            noidungcauhoi = '''Cây cà chua khi trồng có chiều cao %s cm. Tốc độ tăng chiều cao của cây cà chua khi trồng được cho bởi hàm số $v(t)=%st^3+%st^2$, trong đó $t$ tính theo tuần, $v(t)$ tính bằng centimét/tuần. Gọi $h(t)$ (tính bằng centimét) là độ cao của cây cà chua ở tuần thứ $t$. \n'''%(latex(h),latex(a),latex(b))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Chiều cao của cây cà chua ở tuần thứ $t$ là $h(t)=%st^4+%st^3+%s, t\\geq 0$'%(latex(a/4),latex(nsimplify(b/3)),latex(h))
            nb_da_1_s = 'Chiều cao của cây cà chua ở tuần thứ $t$ là $h(t)=%st^4+%st^3+%s, t\\geq 0$'%(latex(a/4),latex(nsimplify(b/3)),latex(h+1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Ta có: $\\displaystyle\\int(%st^3+%st^2)\\text{d}t=\\displaystyle\\int%st^3\\text{d}t+\\displaystyle\\int %st^2\\text{d}t=%st^4+%st^3+\\text{C}$.\\\\ \n'
                        'Do $h(t)$ là một nguyên hàm của $v(t)$ nên $h(t)=%st^4+%st^3+\\text{C}$.\\\\ \n'
                        'Cây cà chua khi trồng có chiều cao $%s$ (cm) nên $h(0)=%s$, suy ra $\\text{C}=%s$.\\\\ \n'
                        'Vậy $h(t)=%st^4+%st^3+%s$.'
                        %(latex(a),latex(b),latex(a),latex(b),latex(a/4),latex(nsimplify(b/3)),latex(a/4),latex(nsimplify(b/3)),latex(h),latex(h),latex(h),latex(a/4),latex(nsimplify(b/3)),latex(h))
                        )

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
            th_da_1_d = '\\True Giai đoạn tăng trưởng của cây kéo dài trong $%s$ tuần'%(latex(t1))
            th_da_1_s = 'Giai đoạn tăng trưởng của cây kéo dài trong $%s$ tuần'%(latex(t1+1))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Cây tăng trưởng khi $v(t)>0$. Xét phương trình $%st^3+%st^2>0$.\\\\ \n'
                        'Ta có: $t^2(%st+%s)>0$, suy ra $%st+%s>0$ nên $t<%s$.\\\\ \n'
                        'Vậy giai đoạn tăng trưởng của cây kéo dài $%s$ tuần.'
                        %(latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(t1),latex(t1))
                        )

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
            vd_da_1_d = '\\True  Chiều cao tối đa của cây cà chua đó là $%s$ (cm)'%(latex(hm))
            vd_da_1_s = ' Chiều cao tối đa của cây cà chua đó là $%s$ (cm)'%(latex(hm+1))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Ta chỉ cần tìm giá trị lớn nhất của $h(t)=%st^4+%st^3+%s$ với $t \\in \\left[0;%s\\right]$.\\\\ \n'
                        'Ta có: $h\'(t)=%st^3+%st^2$ suy ra $h\'(t)=0$ khi $t=0$ hoặc $t=%s$.\\\\ \n'
                        'Ta thấy $h(0)=%s, h\\left(%s\\right)=%s$. Khi đó, $h(t)$ đạt giá lớn nhất bằng $%s$ trên đoạn $\\left[0;%s\\right]$.\\\\ \n'
                        'Vậy chiều cao tối đa của cây cà chua đó là $%s$ (cm).'
                        %(latex(a/4),latex(nsimplify(b/3)),latex(h),latex(t1),latex(a),latex(b),latex(t1),latex(h),latex(t1),latex(hm),latex(hm),latex(t1),latex(hm))
                        )

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
            vdc_da_1_d = '\\True Tại thời điểm cây cà chua đó phát triển nhanh nhất thì cây cà chua cao $%s$ (cm)'%(latex(h2))
            vdc_da_1_s = 'Tại thời điểm cây cà chua đó phát triển nhanh nhất thì cây cà chua cao $%s$ (cm)'%(latex(h2+2))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Ta chỉ cần tìm giá trị lớn nhất của hàm số $v(t)=%st^3+%st^2$ với $t \\in \\left[0;%s\\right]$.\\\\ \n'
                        'Ta có: $v\'(t)=%st^2+%st$ suy ra $v\'(t)=0$ khi $t=0$ hoặc $t=%s$.\\\\ \n'
                        'Ta thấy $v(0)=0, v\\left(%s\\right) \\approx %s,v\\left(%s\\right)=%s $. Khi đó, $v(t)$ đạt giá trị lớn nhất bằng $%s$ trên đoạn $\\left[0;%s\\right]$ tại $t=%s$. Ta có $h\\left(%s \\right) \\approx %s $.\\\\ \n'
                        'Vậy vào thời điểm cây cà chua đó phát triển nhanh nhất thì cây cà chua cao $%s$ (cm).'
                        %(latex(a),latex(b),latex(t1),latex(3*a),latex(2*b),latex(t2),latex(t2),latex(vm),latex(t1),latex(0),latex(vm),latex(t1),latex(t2),latex(t2),latex(h2),latex(h2))
                        )


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
                '\\end{ex}\n \\end{minipage} \n\n').replace('frac','dfrac').replace('+1t','t').replace('.00}','}')
            return content

