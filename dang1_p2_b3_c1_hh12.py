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


def bt_dang1_p2_b3_c1_hh12(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(-5,5)
                b=randint(-5,5)
                x1=randint(-10,10)
                y1=randint(-10,10)
                z1=randint(-10,10)
                x2=randint(-10,10)
                y2=randint(-10,10)
                z2=randint(-10,10)
                x3=randint(-10,10)
                y3=randint(-10,10)
                z3=randint(-10,10)
                while x1**2+y1**2+z1**2==0 or x2**2+y2**2+z2**2==0 or x1**2+y1**2+z1**2==x2**2+y2**2+z2**2==0 or y2==0 or x2==0 or x1/x2==y1/y2 or a==0 or b==0 or x3==x1 or x3==x2:
                    a=randint(-5,5)
                    b=randint(-5,5)
                    x1=randint(-10,10)
                    y1=randint(-10,10)
                    z1=randint(-10,10)
                    x2=randint(-10,10)
                    y2=randint(-10,10)
                    z2=randint(-10,10)
                    x3=randint(-10,10)
                    y3=randint(-10,10)
                    z3=randint(-10,10)
                da=nsimplify(sqrt(x1**2+y1**2+z1**2))
                db=nsimplify(sqrt(x2**2+y2**2+z2**2))
                tvh=x1*x2+y1*y2+z1*z2
                cos=(tvh/(da*db))
                dab=nsimplify(sqrt((x1+x2)**2+(y1+y2)**2+(z1+z2)**2))
                d_ab=nsimplify(sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2))
                x4=nsimplify((x1-x3)/a)
                y4=nsimplify((y1-y3)/b)
                z4=z1-z3
                kq=x4+y4+z4
                kqm=-nsimplify((x2*x3+z3*z2)/y2)
                # Nội dung câu hỏi
                noidungcauhoi = '''Cho hai vectơ $\\vec{a}=(%s;%s;%s)$ và $\\vec{b}=(%s;%s;%s)$.'''%(latex(x1),latex(y1),latex(z1),latex(x2),latex(y2),latex(z2))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Hai vectơ $\\vec{a}$ và $\\vec{b}$ không cùng phương'
                nb_da_1_s = ' Hai vectơ $\\vec{a}$ và $\\vec{b}$ cùng phương'
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True $\\vec{a}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(x1),latex(y1),latex(z1))
                nb_da_2_s = '$\\vec{a}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(-x1),latex(-y1),latex(-z1))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]
                nb_da_2=random.choice(list_nb_da_2)

                nb_da_3_d = '\\True $\\vec{b}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(x2),latex(y2),latex(z2))
                nb_da_3_s = '$\\vec{b}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(-x2),latex(-y2),latex(-z2))
                list_nb_da_3=[nb_da_3_d,nb_da_3_s]
                nb_da_3=random.choice(list_nb_da_3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2, nb_da_3]


                # Nội dung lời giải
                loigiai_nb_1 = ('''Ta có $\\vec{a}=(%s;%s;%s)$ và $\\vec{b}=(%s;%s;%s)$. Vì $\\dfrac{%s}{%s}\\neq\\dfrac{%s}{%s}$ nên hai vectơ $\\vec{a}$ và $\\vec{b}$ không cùng phương.'''%(latex(x1),latex(y1),latex(z1),latex(x2),latex(y2),latex(z2),latex(x1),latex(x2),latex(y1),latex(y2))
                            )
                loigiai_nb_2 = ('''Ta có $\\vec{a}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$.'''%(latex(x1),latex(y1),latex(z1))
                                )
                loigiai_nb_3 = ('''Ta có $\\vec{b}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$.'''%(latex(x2),latex(y2),latex(z2))
                                )

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1, loigiai_nb_2, loigiai_nb_3]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d ='\\True $\\abs{\\vec{a}}=%s$'%(latex(da))
                th_da_1_s = '$\\abs{\\vec{a}}=%s$'%(latex(da+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                th_da_2_d = '\\True $\\abs{\\vec{b}}=%s$'%(latex(db))
                th_da_2_s = '$\\abs{\\vec{b}}=%s$'%(latex(db+1))
                list_th_da_2=[th_da_2_d,th_da_2_s]
                th_da_2=random.choice(list_th_da_2)

                th_da_3_d = '\\True $\\abs{\\vec{a}+\\vec{b}}=%s$'%(latex(dab))
                th_da_3_s = '$\\abs{\\vec{a}+\\vec{b}}=%s$'%(latex(d_ab))
                list_th_da_3=[th_da_3_d,th_da_3_s]
                th_da_3=random.choice(list_th_da_3)

                th_da_4_d = '\\True $\\abs{\\vec{a}-\\vec{b}}=%s$'%(latex(d_ab))
                th_da_4_s = '$\\abs{\\vec{a}-\\vec{b}}=%s$'%(latex(dab))
                list_th_da_4=[th_da_4_d,th_da_4_s]
                th_da_4=random.choice(list_th_da_4)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1, th_da_2, th_da_3, th_da_4]

                # Nội dung lời giải
                loigiai_th_1 =  ('''Ta có $\\abs{\\vec{a}}=\\sqrt{(%s)^2+(%s)^2+(%s)^2}=%s$.'''%(latex(x1),latex(y1),latex(z1),latex(da))
                            )
                loigiai_th_2 =  ('''Ta có $\\abs{\\vec{b}}=\\sqrt{(%s)^2+(%s)^2+(%s)^2}=%s$.'''%(latex(x2),latex(y2),latex(z2),latex(db))
                            )
                loigiai_th_3 =  ('''Ta có $\\vec{a}+\\vec{b}=(%s;%s;%s)$. Suy ra $\\abs{\\vec{a}+\\vec{b}}=%s$.'''%(latex(x1+x2),latex(y1+y2),latex(z1+z2),latex(dab))
                            )
                loigiai_th_4 =  ('''Ta có $\\vec{a}-\\vec{b}=(%s;%s;%s)$. Suy ra $\\abs{\\vec{a}-\\vec{b}}=%s$.'''%(latex(x1-x2),latex(y1-y2),latex(z1-z2),latex(d_ab))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1, loigiai_th_2, loigiai_th_3, loigiai_th_4]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True $%s\\vec{a}+%s\\vec{b}=(%s;%s;%s)$'%(latex(a),latex(b),latex(a*x1+b*x2),latex(a*y1+b*y2),latex(a*z1+b*z2))
                vd_da_1_s = '$%s\\vec{a}+%s\\vec{b}=(%s;%s;%s)$'%(latex(a),latex(b),latex(a*x1+b*x2),latex(a*y1-b*y2),latex(a*z1-b*z2))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True $\\vec{a}\\cdot\\vec{b}=%s$'%(latex(tvh))
                vd_da_2_s = '$\\vec{a}\\cdot\\vec{b}=%s$'%(latex(tvh+1))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]
                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1,vd_da_2]

                # Nội dung lời giải
                loigiai_vd_1 = ('''$%s\\vec{a}+%s\\vec{b}=(%s;%s;%s)$.'''%(latex(a),latex(b),latex(a*x1+b*x2),latex(a*y1+b*y2),latex(a*z1+b*z2))
                            )
                loigiai_vd_2 = ('''$\\vec{a}\\cdot\\vec{b}=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=%s$.'''%(latex(x1),latex(x2),latex(y1),latex(y2),latex(z1),latex(z2),latex(tvh))
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
                vdc_da_1_d = '\\True $\\cos \\left(\\vec{a},\\vec{b}\\right)=%s$'%(latex(cos))
                vdc_da_1_s = '$\\cos \\left(\\vec{a},\\vec{b}\\right)=%s$'%(latex(-cos))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Nếu $\\vec{a}$ bằng $\\vec{c}=(%sx+%s;%sy+%s;z+%s)$ thì $x+y+z=%s$'%(latex(a),latex(x3),latex(b),latex(y3),latex(z3),latex(kq))
                vdc_da_2_s = 'Nếu $\\vec{a}$ bằng $\\vec{c}=(%sx+%s;%sy+%s;z+%s)$ thì $x+y+z=%s$'%(latex(a),latex(x3),latex(b),latex(y3),latex(z3),latex(kq+1))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
                vdc_da_2=random.choice(list_vdc_da_2)

                vdc_da_3_d = '\\True Vectơ $\\vec{b}$ vuông góc với vectơ $\\vec{c}=(%s;m;%s)$ khi và chỉ khi $m=%s$'%(latex(x3),latex(z3),latex(kqm))
                vdc_da_3_s = 'Vectơ $\\vec{b}$ vuông góc với vectơ $\\vec{c}=(%s;m;%s)$ khi $m=%s$'%(latex(x3),latex(z3),latex(kqm+2))
                list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
                vdc_da_3=random.choice(list_vdc_da_3)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1,vdc_da_2,vdc_da_3]

                # Nội dung lời giải
                loigiai_vdc_1 = ('''$\\cos \\left(\\vec{a},\\vec{b}\\right)=\\dfrac{\\vec{a}\\cdot\\vec{b}}{\\abs{\\vec{a}}\\cdot\\abs{\\vec{b}}}=\\dfrac{%s}{%s\\cdot%s}=%s$.'''%(latex(tvh),latex(da),latex(db),latex(cos))
                            )
                loigiai_vdc_2 = ('''Ta có $\\vec{c}=\\vec{a} \\Leftrightarrow \\heva{& %sx+%s=%s \\\\ & %sy+%s=%s \\\\ & z+%s=%s} \\Leftrightarrow \\heva{& x=%s \\\\ & y=%s \\\\ & z=%s}$.\\\\'''
                                '''Vậy $x+y+z=%s$.'''
                                %(latex(a),latex(x3),latex(x1),latex(b),latex(y3),latex(y1),latex(z3),latex(z1),latex(x4),latex(y4),latex(z4),latex(kq))
                            )
                loigiai_vdc_3 = (''' Vectơ $\\vec{b} \\perp \\vec{c} \\Leftrightarrow \\vec{b} \\cdot \\vec{c}=0 \\Leftrightarrow %s\\cdot(%s)+%s\\cdot m+(%s)\\cdot(%s)=0\\Leftrightarrow m=%s$.''' %(latex(x2),latex(x3),latex(y2),latex(z2),latex(z3),latex(kqm))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2,loigiai_vdc_3]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='2':
                # Khai báo biến
                a=randint(-5,5)
                b=randint(-5,5)
                x1=randint(-10,10)
                y1=randint(-10,10)
                k=randint(-3,3)
                z1=randint(-10,10)
                x2=k*x1
                y2=k*y1
                z2=k*z1
                while x1**2+y1**2+z1**2==0 or y1==0 or x1==0 or z1==0 or a==0 or b==0 or k==0:
                    a=randint(-5,5)
                    b=randint(-5,5)
                    x1=randint(-10,10)
                    y1=randint(-10,10)
                    k=randint(-3,3)
                    z1=randint(-10,10)
                    x2=k*x1
                    y2=k*y1
                    z2=k*z1
                da=nsimplify(sqrt(x1**2+y1**2+z1**2))
                db=nsimplify(sqrt(x2**2+y2**2+z2**2))
                tvh=x1*x2+y1*y2+z1*z2
                cos=(tvh/(da*db))

                # Nội dung câu hỏi
                noidungcauhoi = '''Cho hai vectơ $\\vec{a}=(%s;%s;%s)$ và $\\vec{b}=(%s;%s;%s)$.'''%(latex(x1),latex(y1),latex(z1),latex(x2),latex(y2),latex(z2))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Hai vectơ $\\vec{a}$ và $\\vec{b}$ cùng phương'
                nb_da_1_s = ' Hai vectơ $\\vec{a}$ và $\\vec{b}$ không cùng phương'
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True $\\vec{a}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(x1),latex(y1),latex(z1))
                nb_da_2_s = '$\\vec{a}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(-x1),latex(-y1),latex(-z1))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]
                nb_da_2=random.choice(list_nb_da_2)

                nb_da_3_d = '\\True $\\vec{b}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(x2),latex(y2),latex(z2))
                nb_da_3_s = '$\\vec{b}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(-x2),latex(-y2),latex(-z2))
                list_nb_da_3=[nb_da_3_d,nb_da_3_s]
                nb_da_3=random.choice(list_nb_da_3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2, nb_da_3]

                # Nội dung lời giải
                loigiai_nb_1 = ('''Ta có $\\vec{a}=(%s;%s;%s)$ và $\\vec{b}=(%s;%s;%s)$. Vì $\\dfrac{%s}{%s}=\\dfrac{%s}{%s}=\\dfrac{%s}{%s}$ nên hai vectơ $\\vec{a}$ và $\\vec{b}$ không cùng phương.'''%(latex(x1),latex(y1),latex(z1),latex(x2),latex(y2),latex(z2),latex(x1),latex(x2),latex(y1),latex(y2),latex(z1),latex(z2))
                            )
                loigiai_nb_2 = ('''Ta có $\\vec{a}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$.'''%(latex(x1),latex(y1),latex(z1))
                                )
                loigiai_nb_3 = ('''Ta có $\\vec{b}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$.'''%(latex(x2),latex(y2),latex(z2))
                                )
                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1, loigiai_nb_2, loigiai_nb_3]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d ='\\True $\\abs{\\vec{a}}=%s$'%(latex(da))
                th_da_1_s = '$\\abs{\\vec{a}}=%s$'%(latex(da+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                th_da_2_d = '\\True $\\abs{\\vec{b}}=%s$'%(latex(db))
                th_da_2_s = '$\\abs{\\vec{b}}=%s$'%(latex(db+2))
                list_th_da_2=[th_da_2_d,th_da_2_s]

                th_da_2=random.choice(list_th_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1, th_da_2]

                # Nội dung lời giải
                loigiai_th_1 =  ('''Ta có $\\abs{\\vec{a}}=\\sqrt{(%s)^2+(%s)^2+(%s)^2}=%s$.'''%(latex(x1),latex(y1),latex(z1),latex(da))
                            )
                loigiai_th_2 =  ('''Ta có $\\abs{\\vec{b}}=\\sqrt{(%s)^2+(%s)^2+(%s)^2}=%s$.'''%(latex(x2),latex(y2),latex(z2),latex(db))
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
                vd_da_1_d = '\\True $%s\\vec{a}+%s\\vec{b}=(%s;%s;%s)$'%(latex(a),latex(b),latex(a*x1+b*x2),latex(a*y1+b*y2),latex(a*z1+b*z2))
                vd_da_1_s = '$%s\\vec{a}+%s\\vec{b}=(%s;%s;%s)$'%(latex(a),latex(b),latex(a*x1+b*x2),latex(a*y1-b*y2),latex(a*z1-b*z2))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True $\\vec{a}\\cdot\\vec{b}=%s$'%(latex(tvh))
                vd_da_2_s = '$\\vec{a}\\cdot\\vec{b}=%s$'%(latex(tvh+1))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]
                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1,vd_da_2]

                # Nội dung lời giải
                loigiai_vd_1 = ('''$%s\\vec{a}+%s\\vec{b}=(%s;%s;%s)$.'''%(latex(a),latex(b),latex(a*x1+b*x2),latex(a*y1+b*y2),latex(a*z1+b*z2))
                            )
                loigiai_vd_2 = ('''$\\vec{a}\\cdot\\vec{b}=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=%s$.'''%(latex(x1),latex(x2),latex(y1),latex(y2),latex(z1),latex(z2),latex(tvh))
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
                vdc_da_1_d = '\\True $\\cos \\left(\\vec{a},\\vec{b}\\right)=%s$'%(latex(cos))
                vdc_da_1_s = '$\\cos \\left(\\vec{a},\\vec{b}\\right)=%s$'%(latex(-cos))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('''$\\cos \\left(\\vec{a},\\vec{b}\\right)=\\dfrac{\\vec{a}\\cdot\\vec{b}}{\\abs{\\vec{a}}\\cdot\\abs{\\vec{b}}}=\\dfrac{%s}{%s\\cdot%s}=%s$.'''%(latex(tvh),latex(da),latex(db),latex(cos))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            if dang=='3':
                # Khai báo biến
                a=randint(-5,5)
                b=randint(-5,5)
                c=randint(-5,5)
                x1=randint(-10,10)
                y1=randint(-10,10)
                k=randint(-3,3)
                z1=randint(-10,10)
                x2=k*x1
                y2=k*y1
                z2=k*z1
                x3=randint(-10,10)
                y3=randint(-10,10)
                z3=randint(-10,10)
                while x1**2+y1**2+z1**2==0 or x3**2+y3**2+z3**2==0 or x1*x3+y1*y3+z1*z3!=0 or y1==0 or x1==0 or z1==0 or a==0 or b==0 or c==0 or k==0:
                    a=randint(-5,5)
                    b=randint(-5,5)
                    c=randint(-5,5)
                    x1=randint(-10,10)
                    y1=randint(-10,10)
                    k=randint(-3,3)
                    z1=randint(-10,10)
                    x2=k*x1
                    y2=k*y1
                    z2=k*z1
                    x3=randint(-10,10)
                    y3=randint(-10,10)
                    z3=randint(-10,10)
                da=nsimplify(sqrt(x1**2+y1**2+z1**2))
                db=nsimplify(sqrt(x2**2+y2**2+z2**2))
                dc=nsimplify(sqrt(x3**2+y3**2+z3**2))
                tvh_ab=x1*x2+y1*y2+z1*z2
                tvh_bc=x3*x2+y3*y2+z3*z2
                tvh_ac=x3*x1+y3*y1+z3*z1
                cos_ab=(tvh_ab/(da*db))
                cos_bc=(tvh_bc/(db*dc))
                cos_ac=(tvh_ac/(da*dc))
                dabc=nsimplify(sqrt((a*x1+b*x2+c*x3)**2+(a*y1+b*y2+c*y3)**2+(a*z1+b*z2+c*z3)**2))
                # Nội dung câu hỏi
                noidungcauhoi = '''Cho ba vectơ $\\vec{a}=(%s;%s;%s)$, $\\vec{b}=(%s;%s;%s)$ và $\\vec{c}=(%s;%s;%s)$.'''%(latex(x1),latex(y1),latex(z1),latex(x2),latex(y2),latex(z2),latex(x3),latex(y3),latex(z3))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Hai vectơ $\\vec{a}$ và $\\vec{b}$ cùng phương'
                nb_da_1_s = ' Hai vectơ $\\vec{a}$ và $\\vec{b}$ không cùng phương'
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True $\\vec{a}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(x1),latex(y1),latex(z1))
                nb_da_2_s = '$\\vec{a}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(-x1),latex(-y1),latex(-z1))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]
                nb_da_2=random.choice(list_nb_da_2)

                nb_da_3_d = '\\True $\\vec{b}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(x2),latex(y2),latex(z2))
                nb_da_3_s = '$\\vec{b}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(-x2),latex(-y2),latex(-z2))
                list_nb_da_3=[nb_da_3_d,nb_da_3_s]
                nb_da_3=random.choice(list_nb_da_3)

                nb_da_4_d = '\\True $\\vec{c}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(x3),latex(y3),latex(z3))
                nb_da_4_s = '$\\vec{c}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$'%(latex(-x3),latex(-y3),latex(-z3))
                list_nb_da_4=[nb_da_4_d,nb_da_4_s]
                nb_da_4=random.choice(list_nb_da_4)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2, nb_da_3, nb_da_4]

                # Nội dung lời giải
                loigiai_nb_1 = ('''Ta có $\\vec{a}=(%s;%s;%s)$ và $\\vec{b}=(%s;%s;%s)$. Vì $\\dfrac{%s}{%s}=\\dfrac{%s}{%s}=\\dfrac{%s}{%s}$ nên hai vectơ $\\vec{a}$ và $\\vec{b}$ cùng phương.'''%(latex(x1),latex(y1),latex(z1),latex(x2),latex(y2),latex(z2),latex(x1),latex(x2),latex(y1),latex(y2),latex(z1),latex(z2))
                            )
                loigiai_nb_2 = ('''Ta có $\\vec{a}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$.'''%(latex(x1),latex(y1),latex(z1))
                                )
                loigiai_nb_3 = ('''Ta có $\\vec{b}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$.'''%(latex(x2),latex(y2),latex(z2))
                                )
                loigiai_nb_4 = ('''Ta có $\\vec{c}=%s\\vec{i}+%s\\vec{j}+%s\\vec{k}$.'''%(latex(x3),latex(y3),latex(z3))
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
                th_da_1_d ='\\True $\\abs{\\vec{a}}=%s$'%(latex(da))
                th_da_1_s = '$\\abs{\\vec{a}}=%s$'%(latex(da+2))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                th_da_2_d = '\\True $\\abs{\\vec{b}}=%s$'%(latex(db))
                th_da_2_s = '$\\abs{\\vec{b}}=%s$'%(latex(db+1))
                list_th_da_2=[th_da_2_d,th_da_2_s]
                th_da_2=random.choice(list_th_da_2)

                th_da_3_d = '\\True $\\abs{\\vec{c}}=%s$'%(latex(dc))
                th_da_3_s = '$\\abs{\\vec{b}}=%s$'%(latex(dc+1))
                list_th_da_3=[th_da_3_d,th_da_3_s]
                th_da_3=random.choice(list_th_da_3)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1, th_da_2, th_da_3]

                # Nội dung lời giải
                loigiai_th_1 =  ('''Ta có $\\abs{\\vec{a}}=\\sqrt{(%s)^2+(%s)^2+(%s)^2}=%s$.'''%(latex(x1),latex(y1),latex(z1),latex(da))
                            )
                loigiai_th_2 =  ('''Ta có $\\abs{\\vec{b}}=\\sqrt{(%s)^2+(%s)^2+(%s)^2}=%s$.'''%(latex(x2),latex(y2),latex(z2),latex(db))
                            )
                loigiai_th_3 =  ('''Ta có $\\abs{\\vec{c}}=\\sqrt{(%s)^2+(%s)^2+(%s)^2}=%s$.'''%(latex(x3),latex(y3),latex(z3),latex(dc))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1, loigiai_th_2, loigiai_th_3]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True $%s\\vec{a}+%s\\vec{b}=(%s;%s;%s)$'%(latex(a),latex(b),latex(a*x1+b*x2),latex(a*y1+b*y2),latex(a*z1+b*z2))
                vd_da_1_s = '$%s\\vec{a}+%s\\vec{b}=(%s;%s;%s)$'%(latex(a),latex(b),latex(a*x1+b*x2),latex(a*y1-b*y2),latex(a*z1-b*z2))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True $\\vec{a}\\cdot\\vec{b}=%s$'%(latex(tvh_ab))
                vd_da_2_s = '$\\vec{a}\\cdot\\vec{b}=%s$'%(latex(1+tvh_ab))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]
                vd_da_2=random.choice(list_vd_da_2)

                vd_da_3_d = '\\True $\\vec{b}\\cdot\\vec{c}=%s$'%(latex(tvh_bc))
                vd_da_3_s = '$\\vec{b}\\cdot\\vec{c}=%s$'%(latex(1+tvh_bc))
                list_vd_da_3=[vd_da_3_d,vd_da_3_s]
                vd_da_3=random.choice(list_vd_da_3)

                vd_da_4_d = '\\True $\\vec{a}\\cdot\\vec{c}=%s$'%(latex(tvh_ac))
                vd_da_4_s = '$\\vec{a}\\cdot\\vec{c}=%s$'%(latex(1+tvh_ac))
                list_vd_da_4=[vd_da_4_d,vd_da_4_s]
                vd_da_4=random.choice(list_vd_da_4)

                vd_da_5_d = '\\True $%s\\vec{b}+%s\\vec{c}=(%s;%s;%s)$'%(latex(a),latex(b),latex(a*x2+b*x3),latex(a*y2+b*y3),latex(a*z2+b*z3))
                vd_da_5_s = '$%s\\vec{b}+%s\\vec{c}=(%s;%s;%s)$'%(latex(a),latex(b),latex(a*x1+b*x2),latex(a*y1-b*y2),latex(a*z1-b*z2))
                list_vd_da_5=[vd_da_5_d,vd_da_5_s]
                vd_da_5=random.choice(list_vd_da_5)

                vd_da_6_d = '\\True $%s\\vec{a}+%s\\vec{c}=(%s;%s;%s)$'%(latex(a),latex(b),latex(a*x1+b*x3),latex(a*y1+b*y3),latex(a*z1+b*z3))
                vd_da_6_s = '$%s\\vec{a}+%s\\vec{c}=(%s;%s;%s)$'%(latex(a),latex(b),latex(a*x1+b*x2),latex(a*y1-b*y2),latex(a*z1-b*z2))
                list_vd_da_6=[vd_da_6_d,vd_da_6_s]
                vd_da_6=random.choice(list_vd_da_6)

                vd_da_7_d = '\\True $\\vec{a}\\perp\\vec{c}$'
                vd_da_7_s = '$\\vec{a}$ ngược hướng với $\\vec{c}$'
                list_vd_da_7=[vd_da_7_d,vd_da_7_s]
                vd_da_7=random.choice(list_vd_da_7)

                vd_da_8_d = '\\True $\\vec{b}\\perp\\vec{c}$'
                vd_da_8_s = '$\\vec{b}$ cùng hướng với $\\vec{c}$'
                list_vd_da_8=[vd_da_8_d,vd_da_8_s]
                vd_da_8=random.choice(list_vd_da_8)

                vd_da_9_d = '\\True $\\left(\\vec{a},\\vec{c}\\right)=90^{\\circ}$'
                vd_da_9_s = ' $\\left(\\vec{a},\\vec{c}\\right)=45^{\\circ}$'
                list_vd_da_9=[vd_da_9_d,vd_da_9_s]
                vd_da_9=random.choice(list_vd_da_9)

                vd_da_10_d = '\\True $\\left(\\vec{b},\\vec{c}\\right)=90^{\\circ}$'
                vd_da_10_s = ' $\\left(\\vec{b},\\vec{c}\\right)=60^{\\circ}$'
                list_vd_da_10=[vd_da_10_d,vd_da_10_s]
                vd_da_10=random.choice(list_vd_da_10)

                vd_da_11_d = '\\True $\\cos \\left(\\vec{a},\\vec{c}\\right)=0$'
                vd_da_11_s = '$\\cos \\left(\\vec{a},\\vec{c}\\right)=1$'
                list_vd_da_11=[vd_da_11_d,vd_da_11_s]
                vd_da_11=random.choice(list_vd_da_11)

                vd_da_12_d = '\\True $\\cos \\left(\\vec{b},\\vec{c}\\right)=0$'
                vd_da_12_s = '$\\cos \\left(\\vec{b},\\vec{c}\\right)=-1$'
                list_vd_da_12=[vd_da_12_d,vd_da_12_s]
                vd_da_12=random.choice(list_vd_da_12)

                vd_da_13_d = '\\True $\\cos \\left(\\vec{a},\\vec{b}\\right)=%s$'%(latex(cos_ab))
                vd_da_13_s = '$\\cos \\left(\\vec{a},\\vec{b}\\right)=%s$'%(latex(-cos_ab))
                list_vd_da_13=[vd_da_13_d,vd_da_13_s]
                vd_da_13=random.choice(list_vd_da_13)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1,vd_da_2,vd_da_3,vd_da_4,vd_da_5,vd_da_6,vd_da_7,vd_da_8,vd_da_9,vd_da_10,vd_da_11,vd_da_12,vd_da_13]

                # Nội dung lời giải
                loigiai_vd_1 = ('''$%s\\vec{a}+%s\\vec{b}=(%s;%s;%s)$.'''%(latex(a),latex(b),latex(a*x1+b*x2),latex(a*y1+b*y2),latex(a*z1+b*z2))
                            )
                loigiai_vd_2 = ('''$\\vec{a}\\cdot\\vec{b}=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=%s$.'''%(latex(x1),latex(x2),latex(y1),latex(y2),latex(z1),latex(z2),latex(tvh_ab))
                            )
                loigiai_vd_3 = ('''$\\vec{b}\\cdot\\vec{c}=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=%s$.'''%(latex(x2),latex(x3),latex(y2),latex(y3),latex(z2),latex(z3),latex(tvh_bc))
                            )
                loigiai_vd_4 = ('''$\\vec{a}\\cdot\\vec{c}=%s\\cdot(%s)+%s\\cdot(%s)+%s\\cdot(%s)=%s$.'''%(latex(x1),latex(x3),latex(y1),latex(y3),latex(z1),latex(z3),latex(tvh_ac))
                            )
                loigiai_vd_5 = ('''$%s\\vec{b}+%s\\vec{c}=(%s;%s;%s)$.'''%(latex(a),latex(b),latex(a*x2+b*x3),latex(a*y2+b*y3),latex(a*z2+b*z3))
                            )
                loigiai_vd_6 = ('''$%s\\vec{a}+%s\\vec{c}=(%s;%s;%s)$.'''%(latex(a),latex(b),latex(a*x1+b*x3),latex(a*y1+b*y3),latex(a*z1+b*z3))
                            )
                loigiai_vd_7 = ('''Vì $\\vec{a}\\cdot\\vec{c}=0$ nên $\\vec{a}\\perp\\vec{c}$.'''
                            )
                loigiai_vd_8 = ('''Vì $\\vec{b}\\cdot\\vec{c}=0$ nên $\\vec{b}\\perp\\vec{c}$.'''
                            )
                loigiai_vd_9 = ('''Vì $\\vec{a}\\cdot\\vec{c}=0$ nên $\\vec{a}\\perp\\vec{c}$. Suy ra $\\left(\\vec{a},\\vec{c}\\right)=90^{\\circ}$.'''
                            )
                loigiai_vd_10 = ('''Vì $\\vec{b}\\cdot\\vec{c}=0$ nên $\\vec{b}\\perp\\vec{c}$. Suy ra $\\left(\\vec{b},\\vec{c}\\right)=90^{\\circ}$. '''
                            )
                loigiai_vd_11 = ('''Vì $\\vec{a}\\cdot\\vec{c}=0$ nên $\\cos \\left(\\vec{a},\\vec{c}\\right)=0$.'''
                            )
                loigiai_vd_12 = ('''Vì $\\vec{b}\\cdot\\vec{c}=0$ nên $\\cos \\left(\\vec{b},\\vec{c}\\right)=0$.'''
                            )
                loigiai_vd_13 = ('''$\\cos \\left(\\vec{a},\\vec{b}\\right)=\\dfrac{\\vec{a}\\cdot\\vec{b}}{\\abs{\\vec{a}}\\cdot\\abs{\\vec{b}}}=\\dfrac{%s}{%s\\cdot%s}=%s$.'''%(latex(tvh_ab),latex(da),latex(db),latex(cos_ab))
                            )
                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1, loigiai_vd_2,loigiai_vd_3,loigiai_vd_4,loigiai_vd_5,loigiai_vd_6,loigiai_vd_7,loigiai_vd_8,loigiai_vd_9,loigiai_vd_10,loigiai_vd_11,loigiai_vd_12,loigiai_vd_13]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True $\\abs{%s\\vec{a}+%s\\vec{b}+%s\\vec{c}}=%s$'%(latex(a),latex(b),latex(c),latex(dabc))
                vdc_da_1_s = ' $\\abs{%s\\vec{a}+%s\\vec{b}+%s\\vec{c}}=%s$'%(latex(a),latex(b),latex(c),latex(db))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)



                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('''Toạ độ của $%s\\vec{a}+%s\\vec{b}+%s\\vec{c}$ là $(%s;%s;%s)$. Suy ra $\\abs{%s\\vec{a}+%s\\vec{b}+%s\\vec{c}}=%s$.'''%(latex(a),latex(b),latex(c),latex(a*x1+b*x2+c*x3),latex(a*y1+b*y2+c*y3),latex(a*z1+b*z2+c*z3),latex(a),latex(b),latex(c),latex(dabc))
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('1\\vec','\\vec').replace('-1\\vec','-\\vec').replace('+0\\vec{i}','').replace('+0\\vec{j}','').replace('+0\\vec{k}','').replace('+-','-').replace('\\frac','\\dfrac').replace('+0','').replace('1x','x').replace('-1x','x').replace('1y','y').replace('-1y','-y')
            return content

