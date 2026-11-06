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


def bt_dang3_p2_b1_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                b=randint(-9,9)
                c=3+2*b
                d=randint(-20,20)
                y=-x**3+b*x**2+c*x+d
                x_1=-1
                x_2=nsimplify(c/3)
                n=[x_1,x_2]
                sol=sorted(n)
                x1=sol[0]
                x2=sol[1]
                y1=y.subs(x,x1)
                y2=nsimplify(y.subs(x,x2))
                while b==0 or c==0 or x_2==-1 or d==0 or y1>15 or y2<-15:
                    x=symbols('x')
                    b=randint(-9,9)
                    c=3+2*b
                    d=randint(-20,20)
                    y=-x**3+b*x**2+c*x+d
                    x_1=-1
                    x_2=nsimplify(c/3)
                    n=[x_1,x_2]
                    sol=sorted(n)
                    x1=sol[0]
                    x2=sol[1]
                    y1=y.subs(x,x1)
                    y2=nsimplify(y.subs(x,x2))

                # Nội dung câu hỏi
                noidungcauhoi = '''Cho hàm số $y=f(x)=-x^3+%sx^2+%sx+%s$.\n'''%(latex(b),latex(c),latex(d))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Tập xác định của hàm số $f(x)$ là $\\mathscr{D}=\\mathbb{R}$'
                nb_da_1_s = 'Tập xác định của hàm số $f(x)$ là $\\mathscr{D}=\\mathbb{R}\\setminus\\left\\lbrace %s \\right\\rbrace$'%(latex(b))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Tập xác định của hàm số $f(x)$ là $\\mathscr{D}=\\mathbb{R}$.'
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
                th_da_1_d = '\\True Đạo hàm của hàm số $f(x)$ là $f\'(x)=-3x^2+%sx+%s$'%(latex(2*b),latex(c))
                th_da_1_s = 'Đạo hàm của hàm số $f(x)$ là $f\'(x)=-3x^2+%sx+%s$'%(latex(b),latex(c))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Đạo hàm của hàm số $f(x)$ là $f\'(x)=-3x^2+%sx+%s$.'%(latex(2*b),latex(c))
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
                vd_da_1_d = '\\True Hàm số $f(x)$ nghịch biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2))
                vd_da_1_s = 'Hàm số $f(x)$ nghịch biến trên khoảng $(%s;%s)$'%(latex(x1),latex(x2))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True Hàm số $f(x)$ đồng biến trên khoảng $(%s;%s)$'%(latex(x1),latex(x2))
                vd_da_2_s = 'Hàm số $f(x)$ đồng biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]
                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2]

                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có $f\'(x)=-3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow -3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng xét dấu\\\\ \n'
                                '\\hspace*{1cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                                '{$x$/1.3,$f\'(x)$/1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,-,0,+,0,-,}  \n'
                                '\\end{tikzpicture}  \\\\ \n' 
                                'Từ bảng xét dấu ta thấy hàm số $f(x)$ nghịch biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(x1),latex(x2))
                            )
                loigiai_vd_2 = ('Ta có $f\'(x)=-3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow -3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng xét dấu\\\\ \n'
                                '\\hspace*{1cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                                '{$x$/1.3,$f\'(x)$/1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,-,0,+,0,-,}  \n'
                                '\\end{tikzpicture}  \\\\ \n' 
                                'Từ bảng xét dấu ta thấy hàm số $f(x)$ đồng biến trên khoảng $(%s;%s)$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(x1),latex(x2))
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
                vdc_da_1_d = '\\True Hàm số $f(x)$ đạt cực đại tại điểm $x=%s$'%(latex(x2))
                vdc_da_1_s = 'Hàm số $f(x)$ đạt cực đại điểm $x=%s$'%(latex(x1))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Hàm số $f(x)$ đạt cực tiểu tại điểm $x=%s$'%(latex(x1))
                vdc_da_2_s = 'Hàm số $f(x)$ đạt cực tiểu điểm $x=%s$'%(latex(x2))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
                vdc_da_2=random.choice(list_vdc_da_2)

                vdc_da_3_d = '\\True Giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$'%(latex(y2))
                vdc_da_3_s = 'Giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$'%(latex(y1))
                list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
                vdc_da_3=random.choice(list_vdc_da_3)

                vdc_da_4_d = '\\True Giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$'%(latex(y1))
                vdc_da_4_s = 'Giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$'%(latex(y2))
                list_vdc_da_4=[vdc_da_4_d,vdc_da_4_s]
                vdc_da_4=random.choice(list_vdc_da_4)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2,vdc_da_3,vdc_da_4]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có $f\'(x)=-3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow -3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,-,0,+,0,-,}  \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra hàm số $f(x)$ đạt cực đại tại điểm $x=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(x2))
                            )
                loigiai_vdc_2 = ('Ta có $f\'(x)=-3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow -3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,-,0,+,0,-,}  \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra hàm số $f(x)$ đạt cực tiểu tại điểm $x=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(x1))
                            )
                loigiai_vdc_3 = ('Ta có $f\'(x)=-3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow -3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,-,0,+,0,-,}  \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(y2))
                            )
                loigiai_vdc_4 = ('Ta có $f\'(x)=-3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow -3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,-,0,+,0,-,}  \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(y1))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2,loigiai_vdc_3,loigiai_vdc_4]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                b=randint(-9,9)
                c=3-2*b
                d=randint(-20,20)
                y=-x**3+b*x**2+c*x+d
                x_1=1
                x_2=nsimplify(-c/3)
                n=[x_1,x_2]
                sol=sorted(n)
                x1=sol[0]
                x2=sol[1]
                y1=y.subs(x,x1)
                y2=nsimplify(y.subs(x,x2))
                while b==0 or c==0 or x_2==1 or d==0 or y1>15 or y2<-15:
                    x=symbols('x')
                    b=randint(-9,9)
                    c=3-2*b
                    d=randint(-20,20)
                    y=-x**3+b*x**2+c*x+d
                    x_1=1
                    x_2=nsimplify(-c/3)
                    n=[x_1,x_2]
                    sol=sorted(n)
                    x1=sol[0]
                    x2=sol[1]
                    y1=y.subs(x,x1)
                    y2=nsimplify(y.subs(x,x2))

                # Nội dung câu hỏi
                noidungcauhoi = '''Cho hàm số $y=f(x)=-x^3+%sx^2+%sx+%s$.\n'''%(latex(b),latex(c),latex(d))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Tập xác định của hàm số $f(x)$ là $\\mathscr{D}=\\mathbb{R}$'
                nb_da_1_s = 'Tập xác định của hàm số $f(x)$ là $\\mathscr{D}=\\mathbb{R}\\setminus\\left\\lbrace %s \\right\\rbrace$'%(latex(b))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Tập xác định của hàm số $f(x)$ là $\\mathscr{D}=\\mathbb{R}$.'
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
                th_da_1_d = '\\True Đạo hàm của hàm số $f(x)$ là $f\'(x)=-3x^2+%sx+%s$'%(latex(2*b),latex(c))
                th_da_1_s = 'Đạo hàm của hàm số $f(x)$ là $f\'(x)=-3x^2+%sx+%s$'%(latex(b),latex(c))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Đạo hàm của hàm số $f(x)$ là $f\'(x)=-3x^2+%sx+%s$.'%(latex(2*b),latex(c))
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
                vd_da_1_d = '\\True Hàm số $f(x)$ nghịch biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2))
                vd_da_1_s = 'Hàm số $f(x)$ nghịch biến trên khoảng $(%s;%s)$'%(latex(x1),latex(x2))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True Hàm số $f(x)$ đồng biến trên khoảng $(%s;%s)$'%(latex(x1),latex(x2))
                vd_da_2_s = 'Hàm số $f(x)$ đồng biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]
                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2]

                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có $f\'(x)=-3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow -3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng xét dấu\\\\ \n'
                                '\\hspace*{1cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                                '{$x$/1.3,$f\'(x)$/1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,-,0,+,0,-,}  \n'
                                '\\end{tikzpicture}  \\\\ \n' 
                                'Từ bảng xét dấu ta thấy hàm số $f(x)$ nghịch biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(x1),latex(x2))
                            )
                loigiai_vd_2 = ('Ta có $f\'(x)=-3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow -3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng xét dấu\\\\ \n'
                                '\\hspace*{1cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                                '{$x$/1.3,$f\'(x)$/1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,-,0,+,0,-,}  \n'
                                '\\end{tikzpicture}  \\\\ \n' 
                                'Từ bảng xét dấu ta thấy hàm số $f(x)$ đồng biến trên khoảng $(%s;%s)$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(x1),latex(x2))
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
                vdc_da_1_d = '\\True Hàm số $f(x)$ đạt cực đại tại điểm $x=%s$'%(latex(x2))
                vdc_da_1_s = 'Hàm số $f(x)$ đạt cực đại điểm $x=%s$'%(latex(x1))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Hàm số $f(x)$ đạt cực tiểu tại điểm $x=%s$'%(latex(x1))
                vdc_da_2_s = 'Hàm số $f(x)$ đạt cực tiểu điểm $x=%s$'%(latex(x2))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
                vdc_da_2=random.choice(list_vdc_da_2)

                vdc_da_3_d = '\\True Giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$'%(latex(y2))
                vdc_da_3_s = 'Giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$'%(latex(y1))
                list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
                vdc_da_3=random.choice(list_vdc_da_3)

                vdc_da_4_d = '\\True Giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$'%(latex(y1))
                vdc_da_4_s = 'Giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$'%(latex(y2))
                list_vdc_da_4=[vdc_da_4_d,vdc_da_4_s]
                vdc_da_4=random.choice(list_vdc_da_4)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2,vdc_da_3,vdc_da_4]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có $f\'(x)=-3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow -3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,-,0,+,0,-,}  \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra hàm số $f(x)$ đạt cực đại tại điểm $x=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(x2))
                            )
                loigiai_vdc_2 = ('Ta có $f\'(x)=-3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow -3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,-,0,+,0,-,}  \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra hàm số $f(x)$ đạt cực tiểu tại điểm $x=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(x1))
                            )
                loigiai_vdc_3 = ('Ta có $f\'(x)=-3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow -3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,-,0,+,0,-,}  \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(y2))
                            )
                loigiai_vdc_4 = ('Ta có $f\'(x)=-3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow -3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,-,0,+,0,-,}  \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+/$%s$,-/$-\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(y1))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2,loigiai_vdc_3,loigiai_vdc_4]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='3':
                # Khai báo biến
                x=symbols('x')
                b=randint(-9,9)
                c=-3+2*b
                d=randint(-20,20)
                y=x**3+b*x**2+c*x+d
                x_1=-1
                x_2=nsimplify(-c/3)
                n=[x_1,x_2]
                sol=sorted(n)
                x1=sol[0]
                x2=sol[1]
                y1=y.subs(x,x1)
                y2=nsimplify(y.subs(x,x2))
                while b==0 or c==0 or x_2==-1 or d==0 or y1>15 or y2<-15:
                    x=symbols('x')
                    b=randint(-9,9)
                    c=-3+2*b
                    d=randint(-20,20)
                    y=x**3+b*x**2+c*x+d
                    x_1=-1
                    x_2=nsimplify(-c/3)
                    n=[x_1,x_2]
                    sol=sorted(n)
                    x1=sol[0]
                    x2=sol[1]
                    y1=y.subs(x,x1)
                    y2=nsimplify(y.subs(x,x2))

                # Nội dung câu hỏi
                noidungcauhoi = '''Cho hàm số $y=f(x)=x^3+%sx^2+%sx+%s$.\n'''%(latex(b),latex(c),latex(d))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Tập xác định của hàm số $f(x)$ là $\\mathscr{D}=\\mathbb{R}$'
                nb_da_1_s = 'Tập xác định của hàm số $f(x)$ là $\\mathscr{D}=\\mathbb{R}\\setminus\\left\\lbrace %s \\right\\rbrace$'%(latex(b))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Tập xác định của hàm số $f(x)$ là $\\mathscr{D}=\\mathbb{R}$.'
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
                th_da_1_d = '\\True Đạo hàm của hàm số $f(x)$ là $f\'(x)=3x^2+%sx+%s$'%(latex(2*b),latex(c))
                th_da_1_s = 'Đạo hàm của hàm số $f(x)$ là $f\'(x)=3x^2+%sx+%s$'%(latex(b),latex(c))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Đạo hàm của hàm số $f(x)$ là $f\'(x)=3x^2+%sx+%s$.'%(latex(2*b),latex(c))
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
                vd_da_1_d = '\\True Hàm số $f(x)$ đồng biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2))
                vd_da_1_s = 'Hàm số $f(x)$ đồng biến trên khoảng $(%s;%s)$'%(latex(x1),latex(x2))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True Hàm số $f(x)$ nghịch biến trên khoảng $(%s;%s)$'%(latex(x1),latex(x2))
                vd_da_2_s = 'Hàm số $f(x)$ nghịch biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]
                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2]

                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có $f\'(x)=3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow 3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng xét dấu\\\\ \n'
                                '\\hspace*{1cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                                '{$x$/1.3,$f\'(x)$/1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,+,0,-,0,+,}  \n'
                                '\\end{tikzpicture}  \\\\ \n' 
                                'Từ bảng xét dấu ta thấy hàm số $f(x)$ đồng biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(x1),latex(x2))
                            )
                loigiai_vd_2 = ('Ta có $f\'(x)=3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow 3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng xét dấu\\\\ \n'
                                '\\hspace*{1cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                                '{$x$/1.3,$f\'(x)$/1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,+,0,-,0,+,}  \n'
                                '\\end{tikzpicture}  \\\\ \n' 
                                'Từ bảng xét dấu ta thấy hàm số $f(x)$ nghịch biến trên khoảng $(%s;%s)$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(x1),latex(x2))
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
                vdc_da_1_d = '\\True Hàm số $f(x)$ đạt cực đại tại điểm $x=%s$'%(latex(x1))
                vdc_da_1_s = 'Hàm số $f(x)$ đạt cực đại điểm $x=%s$'%(latex(x2))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Hàm số $f(x)$ đạt cực tiểu tại điểm $x=%s$'%(latex(x2))
                vdc_da_2_s = 'Hàm số $f(x)$ đạt cực tiểu điểm $x=%s$'%(latex(x1))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
                vdc_da_2=random.choice(list_vdc_da_2)

                vdc_da_3_d = '\\True Giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$'%(latex(y1))
                vdc_da_3_s = 'Giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$'%(latex(y2))
                list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
                vdc_da_3=random.choice(list_vdc_da_3)

                vdc_da_4_d = '\\True Giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$'%(latex(y2))
                vdc_da_4_s = 'Giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$'%(latex(y1))
                list_vdc_da_4=[vdc_da_4_d,vdc_da_4_s]
                vdc_da_4=random.choice(list_vdc_da_4)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2,vdc_da_3,vdc_da_4]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có $f\'(x)=3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow 3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,+,0,-,0,+,}  \n'
                                '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra hàm số $f(x)$ đạt cực đại tại điểm $x=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(x1))
                            )
                loigiai_vdc_2 = ('Ta có $f\'(x)=3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow 3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,+,0,-,0,+,}  \n'
                                '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra hàm số $f(x)$ đạt cực tiểu tại điểm $x=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(x2))
                            )
                loigiai_vdc_3 = ('Ta có $f\'(x)=3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow 3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,+,0,-,0,+,}  \n'
                                '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(y1))
                            )
                loigiai_vdc_4 = ('Ta có $f\'(x)=3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow 3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,+,0,-,0,+,}  \n'
                                '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(y2))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2,loigiai_vdc_3,loigiai_vdc_4]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang=='4':
                # Khai báo biến
                x=symbols('x')
                b=randint(-9,9)
                c=-3-2*b
                d=randint(-20,20)
                y=x**3+b*x**2+c*x+d
                x_1=1
                x_2=nsimplify(c/3)
                n=[x_1,x_2]
                sol=sorted(n)
                x1=sol[0]
                x2=sol[1]
                y1=y.subs(x,x1)
                y2=nsimplify(y.subs(x,x2))
                while b==0 or c==0 or x_2==1 or d==0 or y1>15 or y2<-15:
                    x=symbols('x')
                    b=randint(-9,9)
                    c=-3-2*b
                    d=randint(-20,20)
                    y=x**3+b*x**2+c*x+d
                    x_1=1
                    x_2=nsimplify(c/3)
                    n=[x_1,x_2]
                    sol=sorted(n)
                    x1=sol[0]
                    x2=sol[1]
                    y1=y.subs(x,x1)
                    y2=nsimplify(y.subs(x,x2))

                # Nội dung câu hỏi
                noidungcauhoi = '''Cho hàm số $y=f(x)=x^3+%sx^2+%sx+%s$.\n'''%(latex(b),latex(c),latex(d))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Tập xác định của hàm số $f(x)$ là $\\mathscr{D}=\\mathbb{R}$'
                nb_da_1_s = 'Tập xác định của hàm số $f(x)$ là $\\mathscr{D}=\\mathbb{R}\\setminus\\left\\lbrace %s \\right\\rbrace$'%(latex(b))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Tập xác định của hàm số $f(x)$ là $\\mathscr{D}=\\mathbb{R}$.'
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
                th_da_1_d = '\\True Đạo hàm của hàm số $f(x)$ là $f\'(x)=3x^2+%sx+%s$'%(latex(2*b),latex(c))
                th_da_1_s = 'Đạo hàm của hàm số $f(x)$ là $f\'(x)=3x^2+%sx+%s$'%(latex(b),latex(c))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Đạo hàm của hàm số $f(x)$ là $f\'(x)=3x^2+%sx+%s$.'%(latex(2*b),latex(c))
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
                vd_da_1_d = '\\True Hàm số $f(x)$ đồng biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2))
                vd_da_1_s = 'Hàm số $f(x)$ đồng biến trên khoảng $(%s;%s)$'%(latex(x1),latex(x2))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True Hàm số $f(x)$ nghịch biến trên khoảng $(%s;%s)$'%(latex(x1),latex(x2))
                vd_da_2_s = 'Hàm số $f(x)$ nghịch biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$'%(latex(x1),latex(x2))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]
                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2]

                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có $f\'(x)=3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow 3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng xét dấu\\\\ \n'
                                '\\hspace*{1cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                                '{$x$/1.3,$f\'(x)$/1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,+,0,-,0,+,}  \n'
                                '\\end{tikzpicture}  \\\\ \n' 
                                'Từ bảng xét dấu ta thấy hàm số $f(x)$ đồng biến trên các khoảng $(-\\infty;%s)$ và $(%s;+\\infty)$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(x1),latex(x2))
                            )
                loigiai_vd_2 = ('Ta có $f\'(x)=3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow 3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng xét dấu\\\\ \n'
                                '\\hspace*{1cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[deltacl=0.5,espcl=2.5,lgt=2]  \n'
                                '{$x$/1.3,$f\'(x)$/1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,+,0,-,0,+,}  \n'
                                '\\end{tikzpicture}  \\\\ \n' 
                                'Từ bảng xét dấu ta thấy hàm số $f(x)$ nghịch biến trên khoảng $(%s;%s)$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(x1),latex(x2))
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
                vdc_da_1_d = '\\True Hàm số $f(x)$ đạt cực đại tại điểm $x=%s$'%(latex(x1))
                vdc_da_1_s = 'Hàm số $f(x)$ đạt cực đại điểm $x=%s$'%(latex(x2))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Hàm số $f(x)$ đạt cực tiểu tại điểm $x=%s$'%(latex(x2))
                vdc_da_2_s = 'Hàm số $f(x)$ đạt cực tiểu điểm $x=%s$'%(latex(x1))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
                vdc_da_2=random.choice(list_vdc_da_2)

                vdc_da_3_d = '\\True Giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$'%(latex(y1))
                vdc_da_3_s = 'Giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$'%(latex(y2))
                list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
                vdc_da_3=random.choice(list_vdc_da_3)

                vdc_da_4_d = '\\True Giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$'%(latex(y2))
                vdc_da_4_s = 'Giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$'%(latex(y1))
                list_vdc_da_4=[vdc_da_4_d,vdc_da_4_s]
                vdc_da_4=random.choice(list_vdc_da_4)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2,vdc_da_3,vdc_da_4]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có $f\'(x)=3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow 3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,+,0,-,0,+,}  \n'
                                '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra hàm số $f(x)$ đạt cực đại tại điểm $x=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(x1))
                            )
                loigiai_vdc_2 = ('Ta có $f\'(x)=3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow 3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,+,0,-,0,+,}  \n'
                                '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra hàm số $f(x)$ đạt cực tiểu tại điểm $x=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(x2))
                            )
                loigiai_vdc_3 = ('Ta có $f\'(x)=3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow 3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,+,0,-,0,+,}  \n'
                                '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra giá trị cực đại của hàm số $f(x)$ là $y_{\\text{CĐ}}=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(y1))
                            )
                loigiai_vdc_4 = ('Ta có $f\'(x)=3x^2+%sx+%s$.\\\\ \n'
                                '$f\'(x)=0 \\Leftrightarrow 3x^2+%sx+%s=0 \\Leftrightarrow  \\hoac{& x=%s \\\\& x=%s.}$\\\\ \n'
                                'Bảng biến thiên\\\\ \n'
                                '\\hspace*{3cm} \\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=2.5,lgt=1.5]  \n'
                                '{$x$/1.3,$f\'(x)$/0.7,$f(x)$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n' 
                                '\\tkzTabLine{,+,0,-,0,+,}  \n'
                                '\\tkzTabVar{-/$-\\infty$,+/$%s$,-/$%s$,+/$+\\infty$} \n'
                                '\\end{tikzpicture}  \\\\ \n'
                                'Từ bảng biến thiên suy ra giá trị cực tiểu của hàm số $f(x)$ là $y_{\\text{CT}}=%s$.'
                                %(latex(2*b),latex(c),latex(2*b),latex(c),latex(x1),latex(x2),latex(x1),latex(x2),latex(y1),latex(y2),latex(y2))
                            )

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2,loigiai_vdc_3,loigiai_vdc_4]

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-','-').replace('+1x','+x').replace('-1x','-x').replace('\\frac','\\dfrac')
            return content

