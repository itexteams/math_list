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


def bt_dang3_p2_b3_c3_hh10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến

                x=symbols('x')
                y=symbols('y')
                a=randint(-9,9)
                b=randint(-9,9)
                x0=randint(1,9)
                y0=randint(-9,9)
                x1=randint(-9,9)
                y1=Rational((a*x0+b*y0-a*x1),b)
                c=-a*x0-b*y0
                c1=b*x0-a*y0

                while a==0 or b==0 or x1==0 or x0==x1:
                    x=symbols('x')
                    y=symbols('y')
                    a=randint(-9,9)
                    b=randint(-9,9)
                    x0=randint(1,9)
                    y0=randint(-9,9)
                    x1=randint(-9,9)
                    y1=Rational((a*x0+b*y0-a*x1),b)
                    c=-a*x0-b*y0
                    c1=b*x0-a*y0

                dt=a*x+b*y+c
                dt11=-b*x+a*y+c1
                kc=abs(-b*x1+a*y1+c1)/sqrt(a**2+b**2)
                kcs=abs(-b*x1+a*y1+c1+1)/sqrt(a**2+b**2)
                kcs2=abs(-b*x1+a*y1+c1-1)/sqrt(a**2+b**2)

                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd(-b, a), c1)
                # Rút gọn các hệ số
                hs_a = -b // gcd
                hs_b = a // gcd
                hs_c = c1 // gcd
                dt1 = hs_a*x+hs_b*y+hs_c
                # Nội dung câu hỏi
                noidungcauhoi = ('Cho đường tròn $(C)$ có tâm $I\\left(%s;%s\\right)$ và tiếp xúc với đường thẳng $\\Delta: %s=0$.'
                                %(latex(x1),latex(y1),latex(dt1)))


                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True $d(I,\\Delta)=%s$'%(latex(kc))
                nb_da_1_s = '$d(I,\\Delta)=%s$'%(latex(kcs))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True $d(I,\\Delta)=%s$'%(latex(kc))
                nb_da_2_s = '$d(I,\\Delta)=%s$'%(latex(kcs2))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]

                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = ('$(C)$ tiếp xúc với $\\Delta$ nên có bán kính\\\\ \n'
                                '$$R=d(I,\\Delta)=\\dfrac{|%s\\cdot(%s)+%s\\cdot(%s)+%s|}{\\sqrt{(%s)^2+(%s)^2}}=%s.$$'
                                %(latex(-b),latex(x1),latex(a),latex(y1),latex(c1),latex(-b),latex(a),latex(kc),)
                            )
                loigiai_nb_2 = ('$(C)$ tiếp xúc với $\\Delta$ nên có bán kính\\\\ \n'
                                '$$R=d(I,\\Delta)=\\dfrac{|%s\\cdot(%s)+%s\\cdot(%s)+%s|}{\\sqrt{(%s)^2+(%s)^2}}=%s.$$'
                                %(latex(-b),latex(x1),latex(a),latex(y1),latex(c1),latex(-b),latex(a),latex(kc),)
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
                th_da_1_d = '\\True Đường tròn $(C)$ có đường kính bằng $%s$ '%(latex(2*kc))
                th_da_1_s = 'Đường tròn $(C)$ có đường kính bằng $%s$ '%(latex(2*kcs))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                th_da_2_d = '\\True Đường tròn $(C)$ có đường kính bằng $%s$ '%(latex(2*kc))
                th_da_2_s = 'Đường tròn $(C)$ có đường kính bằng $%s$ '%(latex(2*kcs2))
                list_th_da_2=[th_da_2_d,th_da_2_s]

                th_da_2=random.choice(list_th_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1, th_da_2]

                # Nội dung lời giải
                loigiai_th_1 = ('Đường tròn $(C)$ có đường kính bằng $2R=2\\cdot %s=%s$. '
                                %(latex(kc),latex(2*kc))
                            )
                loigiai_th_2 = ('Đường tròn $(C)$ có đường kính bằng $2R=2\\cdot %s=%s$. '
                                %(latex(kc),latex(2*kc))
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
                vd_da_1_d = '\\True Phương trình đường tròn $(C): \\left(x-%s\\right)^2+\\left(y-%s\\right)^2=%s$'%(latex(x1),latex(y1),latex(kc**2),)
                vd_da_1_s = 'Phương trình đường tròn $(C): \\left(x-%s\\right)^2+\\left(y-%s\\right)^2=%s$'%(latex(x1),latex(y1),latex(kc**2),)
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True Phương trình đường tròn $(C): \\left(x-%s\\right)^2+\\left(y-%s\\right)^2=%s$'%(latex(x1),latex(y1),latex(kc**2),)
                vd_da_2_s = 'Phương trình đường tròn $(C): \\left(x-%s\\right)^2+\\left(y-%s\\right)^2=%s$'%(latex(x1),latex(y1),latex(kcs**2),)
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]

                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2]

                # Nội dung lời giải
                loigiai_vd_1 = ('Đường tròn $(C)$ có phương trình $\\left(x-%s\\right)^2+\\left(y-%s\\right)^2=%s$.'%(latex(x1),latex(y1),latex(kc**2),)
                            )
                loigiai_vd_2 = ('Đường tròn $(C)$ có phương trình $\\left(x-%s\\right)^2+\\left(y-%s\\right)^2=%s$.'%(latex(x1),latex(y1),latex(kc**2),)
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
                vdc_da_1_d = '\\True Đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có hoành độ lớn hơn $0$'
                vdc_da_1_s = 'Đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có hoành độ nhỏ hơn $0$'
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có hoành độ lớn hơn $0$'
                vdc_da_2_s = 'Đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có hoành độ nhỏ hơn $0$'
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Gọi $d$ là đường thẳng đi qua $I\\left(%s;%s\\right)$ và vuông góc với $\\Delta$ khi đó $d$ có một vectơ pháp tuyến là $\\vec{n}=(%s;%s)$ nên'
                                '$$d:%s\\left(x-%s\\right)+%s\\left(y-%s\\right)=0\\Leftrightarrow %s=0.$$'
                                'Đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có tọa độ là giao điểm của $\\Delta$ và $d$ và là nghiệm của hệ '
                                ' $\\heva{& %s=0 \\\\ & %s=0}\\Leftrightarrow \\heva{& x=%s \\\\ & y=%s}$.\\\\ \n'
                                'Vậy đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có hoành độ lớn hơn $0$.'
                                %(latex(x1),latex(y1),
                                latex(a),latex(b),latex(a),latex(x1),latex(b),latex(y1),latex(dt),
                                latex(dt1),latex(dt),latex(x0),latex(y0),)
                            )
                loigiai_vdc_2 = ('Gọi $d$ là đường thẳng đi qua $I\\left(%s;%s\\right)$ và vuông góc với $\\Delta$ khi đó $d$ có một vectơ pháp tuyến là $\\vec{n}=(%s;%s)$ nên'
                                '$$d:%s\\left(x-%s\\right)+%s\\left(y-%s\\right)=0\\Leftrightarrow %s=0.$$'
                                'Đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có tọa độ là giao điểm của $\\Delta$ và $d$ và là nghiệm của hệ '
                                ' $\\heva{& %s=0 \\\\ & %s=0}\\Leftrightarrow \\heva{& x=%s \\\\ & y=%s}$.\\\\ \n'
                                'Vậy đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có hoành độ lớn hơn $0$.'
                                %(latex(x1),latex(y1),
                                latex(a),latex(b),latex(a),latex(x1),latex(b),latex(y1),latex(dt),
                                latex(dt1),latex(dt),latex(x0),latex(y0),)
                            )
                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            if dang=='2':
                # Khai báo biến

                x=symbols('x')
                y=symbols('y')
                a=randint(-9,9)
                b=randint(-9,9)
                x0=randint(-9,-1)
                y0=randint(-9,9)
                x1=randint(-9,9)
                y1=Rational((a*x0+b*y0-a*x1),b)
                c=-a*x0-b*y0
                c1=b*x0-a*y0

                while a==0 or b==0 or x1==0 or x0==x1:
                    x=symbols('x')
                    y=symbols('y')
                    a=randint(-9,9)
                    b=randint(-9,9)
                    x0=randint(-9,-1)
                    y0=randint(-9,9)
                    x1=randint(-9,9)
                    y1=Rational((a*x0+b*y0-a*x1),b)
                    c=-a*x0-b*y0
                    c1=b*x0-a*y0

                dt=a*x+b*y+c
                dt11=-b*x+a*y+c1
                kc=abs(-b*x1+a*y1+c1)/sqrt(a**2+b**2)
                kcs=abs(-b*x1+a*y1+c1+1)/sqrt(a**2+b**2)
                kcs2=abs(-b*x1+a*y1+c1-1)/sqrt(a**2+b**2)

                # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd(-b, a), c1)
                # Rút gọn các hệ số
                hs_a = -b // gcd
                hs_b = a // gcd
                hs_c = c1 // gcd
                dt1 = hs_a*x+hs_b*y+hs_c
                # Nội dung câu hỏi
                noidungcauhoi = ('Cho đường tròn $(C)$ có tâm $I\\left(%s;%s\\right)$ và tiếp xúc với đường thẳng $\\Delta: %s=0$.'
                                %(latex(x1),latex(y1),latex(dt1)))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True $d(I,\\Delta)=%s$'%(latex(kc))
                nb_da_1_s = '$d(I,\\Delta)=%s$'%(latex(kcs))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True $d(I,\\Delta)=%s$'%(latex(kc))
                nb_da_2_s = '$d(I,\\Delta)=%s$'%(latex(kcs2))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]

                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = ('$(C)$ tiếp xúc với $\\Delta$ nên có bán kính\\\\ \n'
                                '$$R=d(I,\\Delta)=\\dfrac{|%s\\cdot(%s)+%s\\cdot(%s)+%s|}{\\sqrt{(%s)^2+(%s)^2}}=%s.$$'
                                %(latex(-b),latex(x1),latex(a),latex(y1),latex(c1),latex(-b),latex(a),latex(kc),)
                            )
                loigiai_nb_2 = ('$(C)$ tiếp xúc với $\\Delta$ nên có bán kính\\\\ \n'
                                '$$R=d(I,\\Delta)=\\dfrac{|%s\\cdot(%s)+%s\\cdot(%s)+%s|}{\\sqrt{(%s)^2+(%s)^2}}=%s.$$'
                                %(latex(-b),latex(x1),latex(a),latex(y1),latex(c1),latex(-b),latex(a),latex(kc),)
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
                th_da_1_d = '\\True Đường tròn $(C)$ có đường kính bằng $%s$ '%(latex(2*kc))
                th_da_1_s = 'Đường tròn $(C)$ có đường kính bằng $%s$ '%(latex(2*kcs))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                th_da_2_d = '\\True Đường tròn $(C)$ có đường kính bằng $%s$ '%(latex(2*kc))
                th_da_2_s = 'Đường tròn $(C)$ có đường kính bằng $%s$ '%(latex(2*kcs2))
                list_th_da_2=[th_da_2_d,th_da_2_s]

                th_da_2=random.choice(list_th_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1, th_da_2]

                # Nội dung lời giải
                loigiai_th_1 = ('Đường tròn $(C)$ có đường kính bằng $2R=2\\cdot %s=%s$. '
                                %(latex(kc),latex(2*kc))
                            )
                loigiai_th_2 = ('Đường tròn $(C)$ có đường kính bằng $2R=2\\cdot %s=%s$. '
                                %(latex(kc),latex(2*kc))
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
                vd_da_1_d = '\\True Phương trình đường tròn $(C): \\left(x-%s\\right)^2+\\left(y-%s\\right)^2=%s$'%(latex(x1),latex(y1),latex(kc**2),)
                vd_da_1_s = 'Phương trình đường tròn $(C): \\left(x-%s\\right)^2+\\left(y-%s\\right)^2=%s$'%(latex(x1),latex(y1),latex(kc**2),)
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True Phương trình đường tròn $(C): (\\left(x-%s\\right)^2+\\left(y-%s\\right)^2=%s$'%(latex(x1),latex(y1),latex(kc**2),)
                vd_da_2_s = 'Phương trình đường tròn $(C): \\left(x-%s\\right)^2+\\left(y-%s\\right)^2=%s$'%(latex(x1),latex(y1),latex(kcs**2),)
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]

                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2]

                # Nội dung lời giải
                loigiai_vd_1 = ('Đường tròn $(C)$ có phương trình $\\left(x-%s\\right)^2+\\left(y-%s\\right)^2=%s$.'%(latex(x1),latex(y1),latex(kc**2),)
                            )
                loigiai_vd_2 = ('Đường tròn $(C)$ có phương trình $\\left(x-%s\\right)^2+\\left(y-%s\\right)^2=%s$.'%(latex(x1),latex(y1),latex(kc**2),)
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
                vdc_da_1_d = '\\True Đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có hoành độ nhỏ hơn $0$'
                vdc_da_1_s = 'Đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có hoành độ lớn hơn $0$'
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có hoành độ nhỏ hơn $0$'
                vdc_da_2_s = 'Đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có hoành độ lớn hơn $0$'
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Gọi $d$ là đường thẳng đi qua $I\\left(%s;%s\\right)$ và vuông góc với $\\Delta$ khi đó $d$ có một vectơ pháp tuyến là $\\vec{n}=(%s;%s)$ nên'
                                '$$d:%s\\left(x-%s\\right)+%s\\left(y-%s\\right)=0\\Leftrightarrow %s=0.$$'
                                'Đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có tọa độ là giao điểm của $\\Delta$ và $d$ và là nghiệm của hệ '
                                ' $\\heva{& %s=0 \\\\ & %s=0}\\Leftrightarrow \\heva{& x=%s \\\\ & y=%s}$.\\\\ \n'
                                'Vậy đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có hoành độ lớn hơn $0$.'
                                %(latex(x1),latex(y1),
                                latex(a),latex(b),latex(a),latex(x1),latex(b),latex(y1),latex(dt),
                                latex(dt1),latex(dt),latex(x0),latex(y0),)
                            )
                loigiai_vdc_2 = ('Gọi $d$ là đường thẳng đi qua $I\\left(%s;%s\\right)$ và vuông góc với $\\Delta$ khi đó $d$ có một vectơ pháp tuyến là $\\vec{n}=(%s;%s)$ nên'
                                '$$d:%s\\left(x-%s\\right)+%s\\left(y-%s\\right)=0\\Leftrightarrow %s=0.$$'
                                'Đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có tọa độ là giao điểm của $\\Delta$ và $d$ và là nghiệm của hệ '
                                ' $\\heva{& %s=0 \\\\ & %s=0}\\Leftrightarrow \\heva{& x=%s \\\\ & y=%s}$.\\\\ \n'
                                'Vậy đường tròn $(C)$ tiếp xúc với $\\Delta$ tại điểm có hoành độ lớn hơn $0$.'
                                %(latex(x1),latex(y1),
                                latex(a),latex(b),latex(a),latex(x1),latex(b),latex(y1),latex(dt),
                                latex(dt1),latex(dt),latex(x0),latex(y0),)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+')
            return content   

