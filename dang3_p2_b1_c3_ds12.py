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


def bt_dang3_p2_b1_c3_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(2,20)
                b=randint(2,30)
                n=randint(3,15)
                # Nội dung câu hỏi
                noidungcauhoi = '''Cho hàm số $f(x)=\\dfrac{%sx^{%s}+%s}{x}$.'''%(latex(a),latex(n),latex(b))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d =  '\\True $f(x)=%sx^{%s}+\\dfrac{%s}{x}$'%(latex(a),latex(n-1),latex(b))
                nb_da_1_s = '$f(x)=%sx^{%s}+\\dfrac{%s}{x}$'%(latex(a),latex(n),latex(b))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('$f(x)=%sx^{%s}+\\dfrac{%s}{x}$'%(latex(a),latex(n-1),latex(b))
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
                th_da_1_d = '\\True $\\displaystyle\\int f(x) \\text{d}x=%s\\displaystyle\\int x^{%s} \\text{d}x+%s\\displaystyle\\int \\dfrac{1}{x} \\text{d}x$'%(latex(a),latex(n),latex(b))
                th_da_1_s ='$\\displaystyle\\int f(x) \\text{d}x=%s\\displaystyle\\int x^{%s} \\text{d}x+%s\\displaystyle\\int \\dfrac{1}{x} \\text{d}x$'%(latex(a),latex(n),latex(-b))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('$\\displaystyle\\int f(x) \\text{d}x=%s\\displaystyle\\int x^{%s} \\text{d}x+%s\\displaystyle\\int \\dfrac{1}{x} \\text{d}x$.'%(latex(a),latex(n),latex(b)))

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
                vd_da_1_d = '\\True  $\\displaystyle\\int f(x) \\text{d}x=%sx^{%s}+%s\\ln \\abs{x}+\\text{C}$'%(latex(nsimplify(a/n)),latex(n),latex(b))
                vd_da_1_s = ' $\\displaystyle\\int f(x) \\text{d}x=%sx^{%s}+%s\\ln \\abs{x}+\\text{C}$'%(latex(nsimplify(a/n)),latex(n),latex(-b))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = (' $\\displaystyle\\int f(x) \\text{d}x=%sx^{%s}+%s\\ln \\abs{x}+\\text{C}$.'%(latex(nsimplify(a/n)),latex(n),latex(b)))

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
                vdc_da_1_d = '\\True $f\'(x)=%sx^{%s}+\\dfrac{%s}{x^2}$'%(latex(a*(n-1)),latex(n-2),latex(b))
                vdc_da_1_s = '$f\'(x)=%sx^{%s}+\\dfrac{%s}{x^2}$'%(latex(a*(n-1)),latex(n-1),latex(b))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('$f\'(x)=%sx^{%s}+\\dfrac{%s}{x^2}$.'%(latex(a*(n-1)),latex(n-2),latex(b)))


                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='2':
                # Khai báo biến
                a=randint(2,7)
                b=randint(2,6)
                c=randint(-30,30)
                d=randint(-9,9)
                while a==b or c==0 or c%6!=0 or d==0:
                    a=randint(2,7)
                    b=randint(2,6)
                    c=randint(-30,30)
                    d=randint(-9,9)
                e=4
                kc=nsimplify(-c*2/3-d)
                ke=nsimplify(c*(2/3)*e*e**(1/2)+d*e-(2/3)*c-d)
                # Nội dung câu hỏi
                noidungcauhoi = '''Cho hàm số $F(x)$ là nguyên hàm của hàm số $f(x)=%s\\cdot%s^x+%s\\sqrt{x}+%s$.'''%(latex(a),latex(b),latex(c),latex(d))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d =  '\\True $\\displaystyle\\int f(x)\\text{d}x=%s\\displaystyle\\int %s^x\\text{d}x+%s\\displaystyle\\int \\sqrt{x}\\text{d}x+%s\\displaystyle\\int\\text{d}x$'%(latex(a),latex(b),latex(c),latex(d))
                nb_da_1_s = ' $\\displaystyle\\int f(x)\\text{d}x=%s\\displaystyle\\int %s^x\\text{d}x+%s\\displaystyle\\int \\sqrt{x}\\text{d}x+%s\\displaystyle\\int\\text{d}x$'%(latex(a),latex(b),latex(c),latex(-d))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('$\\displaystyle\\int f(x)\\text{d}x=%s\\displaystyle\\int %s^x\\text{d}x+%s\\displaystyle\\int \\sqrt{x}\\text{d}x+%s\\displaystyle\\int\\text{d}x$.'%(latex(a),latex(b),latex(c),latex(d))
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
                th_da_1_d = '\\True $f\'(x)=%s\\cdot%s^x\\ln%s+%s\\cdot\\dfrac{1}{\\sqrt{x}}$'%(latex(a),latex(b),latex(b),latex(nsimplify(c/2)))
                th_da_1_s ='$f\'(x)=%s\\cdot%s^x\\ln%s+%s\\cdot\\dfrac{1}{\\sqrt{x}}$'%(latex(a),latex(b),latex(b),latex(c))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('$f\'(x)=%s\\cdot%s^x\\ln%s+%s\\cdot\\dfrac{1}{\\sqrt{x}}$.'%(latex(a),latex(b),latex(b),latex(nsimplify(c/2)))
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
                vd_da_1_d = '\\True $F(x)=\\dfrac{%s\\cdot%s^x}{\\ln%s}+%sx\\sqrt{x}+%sx+\\text{C}$'%(latex(a),latex(b),latex(b),latex(nsimplify(c*2/3)),latex(d))
                vd_da_1_s = '$F(x)=\\dfrac{%s\\cdot%s^x}{\\ln%s}+%sx\\sqrt{x}+%sx+\\text{C}$'%(latex(a),latex(b),latex(b),latex(nsimplify(c*3/2)),latex(d))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có $F(x)=\\displaystyle\\int f(x)\\text{d}x=%s\\displaystyle\\int %s^x\\text{d}x+%s\\displaystyle\\int \\sqrt{x}\\text{d}x+%s\\displaystyle\\int\\text{d}x$\\\\ \n'
                                'Suy ra $F(x)=\\dfrac{%s\\cdot%s^x}{\\ln%s}+%sx\\sqrt{x}+%sx+\\text{C}$.'%(latex(a),latex(b),latex(c),latex(d),latex(a),latex(b),latex(b),latex(nsimplify(c*2/3)),latex(d))
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
                vdc_da_1_d ='\\True Nếu $F(1)=\\dfrac{%s}{\\ln%s}$ thì $F(%s)=\\dfrac{%s}{\\ln%s}+%s$'%(latex(a*b),latex(b),latex(e),latex(a*b**e),latex(b),latex(ke))
                vdc_da_1_s = 'Nếu $F(1)=\\dfrac{%s}{\\ln%s}$ thì $F(%s)=\\dfrac{%s}{\\ln%s}+%s$'%(latex(a*b),latex(b),latex(e),latex(a*b**e),latex(b),latex(-ke))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có $F(1)=\\dfrac{%s}{\\ln%s}+%s+%s+\\text{C}$ mà theo bài $F(1)=\\dfrac{%s}{\\ln%s}$ nên $\\text{C}=%s$. \\\\ \n'
                                'Suy ra $F(x)=\\dfrac{%s\\cdot%s^x}{\\ln%s}+%sx\\sqrt{x}+%sx+%s$.\\\\ \n'
                                'Vậy $F(%s)=\\dfrac{%s}{\\ln%s}+%s$.'
                                %(latex(a*b),latex(b),latex(nsimplify(2*c/3)),latex(d),latex(a*b),latex(b),latex(kc),
                                latex(a),latex(b),latex(b),latex(nsimplify(c*2/3)),latex(d),latex(kc),
                                latex(e),latex(a*b**e),latex(b),latex(ke))
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
                a=randint(-9,9)
                b=randint(-9,9)
                # Nội dung câu hỏi
                noidungcauhoi = '''Cho hàm số $f(x)=(x+%s)(x+%s)$.'''%(latex(a),latex(b))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d =  '\\True $f(x)=x^2+%sx+%s$'%(latex(a+b),latex(a*b))
                nb_da_1_s = '$f(x)=x^2+%sx+%s$'%(latex(a-b),latex(a*b))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Ta có $f(x)=x^2+%sx+%sx+%s=x^2+%sx+%s$ .'%(latex(b),latex(a),latex(a*b),latex(a+b),latex(a*b))
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
                th_da_1_d = '\\True $f\'(x)=2x+%s$'%(latex(a+b))
                th_da_1_s ='$f\'(x)=2x+%s$'%(latex(a-b))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('$f\'(x)=2x+%s$.'%(latex(a+b))
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
                vd_da_1_d = '\\True $\\displaystyle\\int f(x) \\text{d}x=\\displaystyle\\int x^2 \\text{d}x+%s\\displaystyle\\int x \\text{d}x+%s\\displaystyle\\int \\text{d}x$'%(latex(a+b),latex(a*b))
                vd_da_1_s = '$\\displaystyle\\int f(x) \\text{d}x=\\displaystyle\\int (x+%s) \\text{d}x \\cdot \\displaystyle\\int  (x+%s) \\text{d}x$'%(latex(a),latex(b))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('$\\displaystyle\\int f(x) \\text{d}x=\\displaystyle\\int x^2 \\text{d}x+%s\\displaystyle\\int x \\text{d}x+%s\\displaystyle\\int \\text{d}x$.'%(latex(a+b),latex(a*b))
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
                vdc_da_1_d ='\\True $\\displaystyle\\int f(x) \\text{d}x=\\dfrac{x^3}{3}+%sx^2+%sx+\\text{C}$'%(latex(nsimplify((a+b)/2)),latex(a*b))
                vdc_da_1_s = '$\\displaystyle\\int f(x) \\text{d}x=x^3+%sx^2+%sx+\\text{C}$'%(latex(nsimplify((a+b)/2)),latex(a*b))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có $\\displaystyle\\int f(x) \\text{d}x=\\displaystyle\\int x^2 \\text{d}x+%s\\displaystyle\\int x \\text{d}x+%s\\displaystyle\\int \\text{d}x$.\\\\ \n'
                                'Suy ra $\\displaystyle\\int f(x) \\text{d}x=\\dfrac{x^3}{3}+%sx^2+%sx+\\text{C}$.'%(latex(a+b),latex(a*b),latex(nsimplify((a+b)/2)),latex(a*b))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='4':
                # Khai báo biến
                a=randint(-20,20)
                b=randint(-20,30)
                m=randint(2,9)
                n=randint(3,9)
                e=2
                while a==b or a==1 or a==-1 or m<=n+1 or b==0 or a==0 or b-a/(m-n+1)==0 or a/(m-n+1)==1 or  a%(m-n+1)!=0 or  a/(m-n+1)==-1:
                    a=randint(-20,20)
                    b=randint(-20,30)
                    m=randint(2,15)
                    n=randint(3,15)
                    e=2
                ke=nsimplify((a/(m-n+1))*e**(m-n+1)-b/e+b)
                kc=b
                # Nội dung câu hỏi
                noidungcauhoi = '''Cho hàm số $F(x)$ là nguyên hàm của hàm số $f(x)=\\dfrac{%sx^{%s}+%sx^{%s}}{x^{%s}}$.'''%(latex(a),latex(m),latex(b),latex(n-2),latex(n))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d =  '\\True $f(x)=%sx^{%s}+%s\\cdot\\dfrac{1}{x^2}$'%(latex(a),latex(m-n),latex(b))
                nb_da_1_s = '$f(x)=%sx^{%s}+%s\\cdot\\dfrac{1}{x^2}$'%(latex(a),latex(m-n),latex(-b))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Ta có $f(x)=%s\\cdot\\dfrac{x^{%s}}{x^{%s}}+%s\\cdot\\dfrac{x^{%s}}{x^{%s}}=%sx^{%s}+%s\\cdot\\dfrac{1}{x^2}$.'%(latex(a),latex(m),latex(n),latex(b),latex(n-2),latex(n),latex(a),latex(m-n),latex(b))
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
                th_da_1_d = '\\True $f\'(x)=%sx^{%s}+%s\\cdot\\dfrac{1}{x^3}$'%(latex(a*(m-n)),latex(m-n-1),latex(-2*b))
                th_da_1_s ='$f\'(x)=%sx^{%s}+%s\\cdot\\dfrac{1}{x^3}$'%(latex(a*(m-n)),latex(m-n-1),latex(-b))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('$f\'(x)=%sx^{%s}+%s\\cdot\\dfrac{1}{x^3}$.'%(latex(a*(m-n)),latex(m-n-1),latex(-2*b))
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
                vd_da_1_d = '\\True $F(x)=%sx^{%s}+%s\\cdot\\dfrac{1}{x}+\\text{C}$'%(latex(Rational(a,m-n+1)),latex(m-n+1),latex(-b))
                vd_da_1_s = '$F(x)=%sx^{%s}+%s\\cdot\\dfrac{1}{x}+\\text{C}$'%(latex(nsimplify(a/(m-n+1))),latex(m-n+1),latex(b))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = (' $F(x)=\\displaystyle\\int f(x) \\text{d}x=\\displaystyle\\int\\left(%sx^{%s}+%s\\cdot\\dfrac{1}{x^2}\\right)\\text{d}x=%sx^{%s}+%s\\cdot\\dfrac{1}{x}+\\text{C}$.'%(latex(a),latex(m-n),latex(b),latex(nsimplify(a/(m-n+1))),latex(m-n+1),latex(-b)))

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
                vdc_da_1_d = '\\True Nếu $F(1)=%s$ thì $F(%s)=%s$'%(latex(Rational(a,m-n+1)),latex(e),latex(ke))
                vdc_da_1_s = ' Nếu $F(1)=%s$ thì $F(%s)=%s$'%(latex(Rational(a,m-n+1)),latex(e),latex(-ke))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có $F(1)=%s-%s+\\text{C}$ mà theo bài ta có $F(%s)=%s$ nên $\\text{C}=%s$.\\\\ \n'
                                'Suy ra $F(x)=%sx^{%s}+%s\\cdot\\dfrac{1}{x}+%s$.\\\\ \n'
                                'Vậy $F(%s)=%s$.'
                                %(latex(Rational(a,m-n+1)),latex(b),latex(e),latex(Rational(a,m-n+1)),latex(b),latex(Rational(a,m-n+1)),latex(m-n+1),latex(-b),latex(Rational(a,m-n+1)),latex(e),latex(ke)))


                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='5':
                # Khai báo biến
                a=randint(2,20)
                b=randint(-30,-2)
                n=randint(3,15)
                # Nội dung câu hỏi
                noidungcauhoi = '''Cho hàm số $f(x)=\\dfrac{%sx^{%s}+%s}{x}$.'''%(latex(a),latex(n),latex(b))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d =  '\\True $f(x)=%sx^{%s}-\\dfrac{%s}{x}$'%(latex(a),latex(n-1),latex(-b))
                nb_da_1_s = '$f(x)=%sx^{%s}+\\dfrac{%s}{x}$'%(latex(a),latex(n-1),latex(-b))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('$f(x)=%sx^{%s}-\\dfrac{%s}{x}$.'%(latex(a),latex(n-1),latex(-b))
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
                th_da_1_d = '\\True $\\displaystyle\\int f(x) \\text{d}x=%s\\displaystyle\\int x^{%s} \\text{d}x+%s\\displaystyle\\int \\dfrac{1}{x} \\text{d}x$'%(latex(a),latex(n-1),latex(b))
                th_da_1_s ='$\\displaystyle\\int f(x) \\text{d}x=%s\\displaystyle\\int x^{%s} \\text{d}x+%s\\displaystyle\\int \\dfrac{1}{x} \\text{d}x$'%(latex(a),latex(n-1),latex(-b))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('$\\displaystyle\\int f(x) \\text{d}x=%s\\displaystyle\\int x^{%s} \\text{d}x+%s\\displaystyle\\int \\dfrac{1}{x} \\text{d}x$.'%(latex(a),latex(n-1),latex(b)))

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
                vd_da_1_d = '\\True  $\\displaystyle\\int f(x) \\text{d}x=%sx^{%s}+%s\\ln \\abs{x}+\\text{C}$'%(latex(nsimplify(a/n)),latex(n),latex(b))
                vd_da_1_s = '$\\displaystyle\\int f(x) \\text{d}x=%sx^{%s}+%s\\ln \\abs{x}+\\text{C}$'%(latex(nsimplify(a/n)),latex(n),latex(-b))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('$\\displaystyle\\int f(x) \\text{d}x=%sx^{%s}+%s\\ln \\abs{x}+\\text{C}$.'%(latex(nsimplify(a/n)),latex(n),latex(b)))

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
                vdc_da_1_d = '\\True $f\'(x)=%sx^{%s}-\\dfrac{%s}{x^2}$'%(latex(a*(n-1)),latex(n-2),latex(b))
                vdc_da_1_s = '$f\'(x)=%sx^{%s}-\\dfrac{%s}{x^2}$'%(latex(a*(n-1)),latex(n-1),latex(b))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('$f\'(x)=%sx^{%s}-\\dfrac{%s}{x^2}$.'%(latex(a*(n-1)),latex(n-2),latex(b)))


                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            if dang=='6':
                # Khai báo biến
                a=randint(-5,5)
                b=randint(-9,9)
                c=randint(-5,5)
                d=randint(-9,9)
                while a==0 or b==0 or c==0 or d==0 or c==-d:
                    a=randint(-5,5)
                    b=randint(-9,9)
                    c=randint(-5,5)
                    d=randint(-9,9)
                # Nội dung câu hỏi
                noidungcauhoi = '''Cho hàm số $f(x)=\\dfrac{%se^{2x}+%se^x+%s}{%se^x+%s}$.'''%(latex(a*c),latex(a*d+b*c),latex(b*d),latex(c),latex(d))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d =  '\\True $f(x)=%se^x+%s$'%(latex(a),latex(b))
                nb_da_1_s = '$f(x)=%se^x+%s$'%(latex(c),latex(d))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Ta có\\\\ \n'
                                '\\begin{eqnarray*}\n'
                                '%se^{2x}+%se^x+%s&=&%se^{2x}+%se^x+%se^x+%s\\\\ \n'
                                '&=&%se^x\\left(%se^x+%s\\right)+%s\\left(%se^x+%s\\right)\\\\ \n'
                                '&=&\\left(%se^x+%s\\right)\\left(%se^x+%s\\right). \n'
                                '\\end{eqnarray*}\n'
                                'Suy ra $f(x)=\\dfrac{%se^{2x}+%se^x+%s}{%se^x+%s}=\\dfrac{\\left(%se^x+%s\\right)\\left(%se^x+%s\\right)}{%se^x+%s}=%se^x+%s$.\\\\ \n'
                                'Vậy $f(x)=%se^x+%s$.'%(latex(a*c),latex(a*d+b*c),latex(b*d),latex(a*c),latex(b*d),latex(b*c),latex(b*d),latex(a),latex(c),
                                latex(d),latex(b),latex(c),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a*c),latex(a*d+b*c),latex(b*d),latex(c),latex(d),
                                latex(a),latex(b),latex(c),latex(d),latex(c),latex(d),latex(a),latex(b),latex(a),latex(b))
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
                th_da_1_d = '\\True $f\'(x)=%se^x$'%(latex(a))
                th_da_1_s ='$f\'(x)=%se^x$'%(latex(-a))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('$f\'(x)=%se^x$.'%(latex(a))
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
                vd_da_1_d = '\\True $f\'(x)-f\'\'(x)=0$'
                vd_da_1_s = '$f\'(x)-f\'\'(x)=%se^x$'%(latex(2*a))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có $f\'\'(x)=%se^x=f\'(x)$\\\\ \n'
                                'Suy ra $f\'(x)-f\'\'(x)=0$.'%(latex(a))
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
                vdc_da_1_d ='\\True $\\displaystyle\\int f(x) \\text{d}x=%se^x+%sx+\\text{C}$'%(latex(a),latex(b))
                vdc_da_1_s = '$\\displaystyle\\int f(x) \\text{d}x=%se^{2x}+%sx+\\text{C}$'%(latex(a),latex(b))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có $\\displaystyle\\int f(x) \\text{d}x=\\displaystyle\\int %se^x \\text{d}x+%s\\displaystyle\\int\\text{d}x$.\\\\ \n'
                                'Suy ra $\\displaystyle\\int f(x) \\text{d}x=%se^x+%sx+\\text{C}$.'%(latex(a),latex(b),latex(a),latex(b))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='7':
                # Khai báo biến
                a=randint(-50,50)
                b=randint(-40,40)
                while a==0 or b==0 or a%4!=0 or b%2!=0:
                    a=randint(-50,50)
                    b=randint(-40,40)
                a1=nsimplify(a/4)
                b1=nsimplify(b/3)
                # Nội dung câu hỏi
                noidungcauhoi = '''Cho hàm số $f(x)=%sx^3+%sx^2$.'''%(latex(a),latex(b))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d =  '\\True $\\displaystyle\\int f(x) \\text{d}x=%s\\displaystyle\\int x^3 \\text{d}x+%s\\displaystyle\\int x^2 \\text{d}x$'%(latex(a),latex(b))
                nb_da_1_s = '$\\displaystyle\\int f(x) \\text{d}x=%s\\displaystyle\\int x^3 \\text{d}x+%s\\displaystyle\\int x^2 \\text{d}x$'%(latex(a1),latex(b1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('$\\displaystyle\\int f(x) \\text{d}x=%s\\displaystyle\\int x^3 \\text{d}x+%s\\displaystyle\\int x^2 \\text{d}x$.'%(latex(a),latex(b))
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
                th_da_1_d = '\\True $f\'(x)=%sx^2+%sx$'%(latex(3*a),latex(2*b))
                th_da_1_s ='$f\'(x)=%sx^2+%sx$'%(latex(3*a),latex(b))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('$f\'(x)=%sx^2+%sx$.'%(latex(3*a),latex(2*b))
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
                vd_da_1_d = '\\True $\\displaystyle\\int f(x) \\text{d}x=%sx^4+%sx^3+\\text{C}$'%(latex(a1),latex(b1))
                vd_da_1_s = '$\\displaystyle\\int f(x) \\text{d}x=%sx^4+%sx^3+\\text{C}$'%(latex(a),latex(b))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('$\\displaystyle\\int f(x) \\text{d}x=%sx^4+%sx^3+\\text{C}$.'%(latex(a1),latex(b1))
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
                vdc_da_1_d ='\\True $f\'\'(x)=%sx+%s$'%(latex(6*a),latex(2*b))
                vdc_da_1_s = '$f\'\'(x)=%sx+%s$'%(latex(3*a),latex(2*b))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có $f\'(x)=%sx^2+%sx$\\\\ \n'
                            'Suy ra $f\'\'(x)=%sx+%s$.'%(latex(3*a),latex(2*b),latex(6*a),latex(2*b))
                            )


                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='8':
                # Khai báo biến
                a=randint(-8,8)
                b=randint(-9,9)
                c=randint(-5,5)
                d=randint(-9,9)
                k=randint(-10,10)
                e=randint(-6,6)
                while a==0 or b==0 or c==0 or d==0 or c==-d or a%2!=0 or c==1 or c==-1 or k==0:
                    a=randint(-5,5)
                    b=randint(-9,9)
                    c=randint(-5,5)
                    d=randint(-9,9)
                    k=randint(-10,10)
                    e=randint(-6,6)
                kc=nsimplify(k-a/2-b)
                ke=nsimplify((a/2)*e**2+b*e+kc)
                # Nội dung câu hỏi
                noidungcauhoi = '''Cho hàm số $F(x)$ là nguyên hàm của hàm số $f(x)=\\dfrac{%sx^2+%sx+%s}{%sx+%s}$.'''%(latex(a*c),latex(a*d+b*c),latex(b*d),latex(c),latex(d))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d =  '\\True $f(x)=%sx+%s$'%(latex(a),latex(b))
                nb_da_1_s = '$f(x)=%sx+%s$'%(latex(-a),latex(-b))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Ta có\\\\ \n'
                                '\\begin{eqnarray*}\n'
                                '%sx^2+%sx+%s&=&%sx^2+%sx+%sx+%s\\\\ \n'
                                '&=&%sx\\left(%sx+%s\\right)+%s\\left(%sx+%s\\right)\\\\ \n'
                                '&=&\\left(%sx+%s\\right)\\left(%sx+%s\\right). \n'
                                '\\end{eqnarray*}\n'
                                'Suy ra $f(x)=\\dfrac{%sx^2+%sx+%s}{%sx+%s}=\\dfrac{\\left(%sx+%s\\right)\\left(%sx+%s\\right)}{%sx+%s}=%sx+%s$.\\\\ \n'
                                'Vậy $f(x)=%sx+%s$.'%(latex(a*c),latex(a*d+b*c),latex(b*d),latex(a*c),latex(b*d),latex(b*c),latex(b*d),latex(a),latex(c),
                                latex(d),latex(b),latex(c),latex(d),latex(a),latex(b),latex(c),latex(d),latex(a*c),latex(a*d+b*c),latex(b*d),latex(c),latex(d),
                                latex(a),latex(b),latex(c),latex(d),latex(c),latex(d),latex(a),latex(b),latex(a),latex(b))
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
                th_da_1_d = '\\True $f\'(x)=%s$'%(latex(a))
                th_da_1_s ='$f\'(x)=%s$'%(latex(-a))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('$f\'(x)=%s$.'%(latex(a))
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
                vd_da_1_d ='\\True $F(x)=%sx^2+%sx+\\text{C}$'%(latex(nsimplify(a/2)),latex(b))
                vd_da_1_s = '$F(x)=%sx^2+%sx+\\text{C}$'%(latex(a),latex(b))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có $F(x)=\\displaystyle\\int f(x) \\text{d}x=%s\\displaystyle\\int x \\text{d}x+%s\\displaystyle\\int\\text{d}x$.\\\\ \n'
                                'Suy ra $F(x)=%sx^2+%sx+\\text{C}$.'%(latex(a),latex(b),latex(nsimplify(a/2)),latex(b))
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
                vdc_da_1_d ='\\True Nếu $F(1)=%s$ thì $F(%s)=%s$' %(latex(k),latex(e),latex(ke))
                vdc_da_1_s = 'Nếu $F(1)=%s$ thì $F(%s)=%s$' %(latex(k),latex(e),latex(ke))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có $F(1)=%s+\\text{C}$ mà theo bài $F(1)=%s$ nên $\\text{C}=%s$.\\\\ \n'
                                'Suy ra $F(x)=%sx^2+%sx+%s$.\\\\ \n'
                                'Vậy $F(%s)=%s$.'%(latex(nsimplify(a/2+b)),latex(k),latex(kc),latex(nsimplify(a/2)),latex(b),latex(kc),latex(e),latex(ke))
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-').replace('--','+').replace('-1x','-x').replace('+1x','+x').replace('-1\\displaystyle','-\\displaystyle').replace('+1\\displaystyle','+\\displaystyle').replace('-1e','-e').replace('+1e','+e').replace('x^{1}','x').replace('+1\\cdot','+').replace('-1\\cdot','-')
            return content

