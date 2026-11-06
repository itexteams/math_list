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


def bt_dang1_p2_b4_c2_hh10(self):
            # Khai báo biến
            lis1=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
            xa=random.choice(lis1)
            ya=random.choice(lis1)
            xb=random.choice(lis1)
            yb=random.choice(lis1)
            while xa*yb==xb*ya:
                xa=random.choice(lis1)
                ya=random.choice(lis1)
                xb=random.choice(lis1)
                yb=random.choice(lis1)

            k=random.choice(lis1)

            a=random.choice(lis1)
            b=random.choice(lis1)

            c=random.choice(lis1)
            d=random.choice(lis1)

            x0=random.choice(lis1)
            h=sqrt((a*x0+b)**2+(c*x0+d)**2)

            x=symbols('x')
            pt=(a**2+c**2)*x**2+(2*a*b+2*c*d)*x+b**2+d**2-h**2

            x1=Rational(b**2+d**2-h**2,x0*a**2+x0*c**2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong mặt phẳng $(Oxy)$, cho $\\vec{a}=%s \\vec{i}+%s \\vec{j}$ và $\\vec{b}=%s \\vec{i}+%s \\vec{j}$. \n'''
                            %(latex(xa),latex(ya),latex(xb),latex(yb))
                            )

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Tọa độ của vectơ $\\vec{a}$ là $(%s; %s)$' %(latex(xa),latex(ya))
            nb_da_1_s = 'Tọa độ của vectơ $\\vec{a}$ là $(%s; %s)$' %(latex(xa),latex(ya+1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Tọa độ của vectơ $\\vec{b}$ là $(%s; %s)$' %(latex(xb),latex(yb))
            nb_da_2_s = 'Tọa độ của vectơ $\\vec{b}$ là $(%s; %s)$' %(latex(xb),latex(yb-1))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]

            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Tọa độ của vectơ $\\vec{a}$ là $(%s; %s)$.' %(latex(xa),latex(ya))
                        )
            loigiai_nb_2 = ('Tọa độ của vectơ $\\vec{b}$ là $(%s; %s)$.' %(latex(xb),latex(yb))
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
            th_da_1_d = '\\True $\\vec{a}+\\vec{b}=(%s; %s)$' %(latex(xa+xb),latex(ya+yb))
            th_da_1_s = '$\\vec{a}+\\vec{b}=(%s; %s)$' %(latex(xa+xb),latex(ya+yb+1))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $\\vec{a}-\\vec{b}=(%s; %s)$' %(latex(xa-xb),latex(ya-yb))
            th_da_2_s = '$\\vec{a}-\\vec{b}=(%s; %s)$' %(latex(xa-xb),latex(ya-yb+1))
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            th_da_3_d = '\\True $%s \\vec{a}=(%s; %s)$' %(latex(k),latex(k*xa),latex(k*ya))
            th_da_3_s = '$%s \\vec{a}=(%s; %s)$' %(latex(k),latex(k*xa),latex(k*ya+1))
            list_th_da_3=[th_da_3_d,th_da_3_s]
            th_da_3=random.choice(list_th_da_3)

            th_da_4_d = '\\True $%s \\vec{a}+%s\\vec{b}=(%s; %s)$' %(latex(c),latex(d),latex(c*xa+d*xb),latex(c*ya+d*yb))
            th_da_4_s = '$%s \\vec{a}+%s\\vec{b}=(%s; %s)$' %(latex(c),latex(d),latex(c*xa+d*xb),latex(c*ya+d*yb+1))
            list_th_da_4=[th_da_4_d,th_da_4_s]
            th_da_4=random.choice(list_th_da_4)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2,th_da_3,th_da_4]

            # Nội dung lời giải
            loigiai_th_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\vec{a}=(%s; %s)$. \\\\ \n'
                            '\\hspace*{1cm} $\\vec{b}=(%s; %s)$. \\\\ \n'
                            '\\hspace*{1cm} $\\vec{a}+\\vec{b}=(%s; %s)$.' 
                            %(latex(xa),latex(ya),
                            latex(xb),latex(yb),
                            latex(xa+xb),latex(ya+yb)
                        ))
            loigiai_th_2 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\vec{a}=(%s; %s)$. \\\\ \n'
                            '\\hspace*{1cm} $\\vec{b}=(%s; %s)$. \\\\ \n'
                            '\\hspace*{1cm} $\\vec{a}-\\vec{b}=(%s; %s)$.' 
                            %(latex(xa),latex(ya),
                            latex(xb),latex(yb),
                            latex(xa-xb),latex(ya-yb)
                        ))
            loigiai_th_3 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\vec{a}=(%s; %s)$. \\\\ \n'
                            '\\hspace*{1cm} $%s \\vec{a}=(%s; %s)$.'
                            %(latex(xa),latex(ya),
                            latex(k),latex(k*xa),latex(k*ya),
                        ))
            loigiai_th_4 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\vec{a}=(%s; %s)$ suy ra $%s \\vec{a}=(%s; %s)$. \\\\ \n'
                            '\\hspace*{1cm} $\\vec{b}=(%s; %s)$ suy ra $%s \\vec{b}=(%s; %s)$. \\\\ \n'
                            '\\hspace*{1cm} $%s \\vec{a}+%s\\vec{b}=(%s; %s)$.' 
                            %(latex(xa),latex(ya),latex(c),latex(c*xa),latex(c*ya),
                            latex(xb),latex(yb),latex(d),latex(d*xb),latex(d*yb),
                            latex(c),latex(d),latex(c*xa+d*xb),latex(c*ya+d*yb)
                        ))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2,loigiai_th_3,loigiai_th_4]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Vectơ $\\vec{u}=(x+%s; y+%s)$ bằng vectơ $\\vec{a}$ khi $x=%s, y=%s$' %(latex(a),latex(b),latex(xa-a),latex(ya-b))
            vd_da_1_s = 'Vectơ $\\vec{u}=(x+%s; y+%s)$ bằng vectơ $\\vec{a}$ khi $x=%s, y=%s$' %(latex(a),latex(b),latex(xa-a),latex(ya-b+1))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Hai vectơ $\\vec{a}$ và $\\vec{b}$ không cùng phương'
            vd_da_2_s = 'Hai vectơ $\\vec{a}$ và $\\vec{b}$ cùng phương'
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]

            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\vec{a}=(%s; %s)$. \\\\ \n'
                            '\\hspace*{1cm} $\\vec{u}=\\vec{a} \\Leftrightarrow \\heva{& x+%s=%s\\\\& y+%s=%s} \\Leftrightarrow \\heva{& x=%s\\\\& y=%s}$.'
                            %(latex(xa),latex(ya),
                            latex(a),latex(xa),latex(b),latex(ya),latex(xa-a),latex(ya-b)

                        ))
            loigiai_vd_2 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\vec{a}=(%s; %s)$. \\\\ \n'
                            '\\hspace*{1cm} $\\vec{b}=(%s; %s)$. \\\\ \n'
                            'Ta thấy $\\dfrac{%s}{%s} \\ne \\dfrac{%s}{%s}$ nên hai vectơ không cùng phương.' 
                            %(latex(xa),latex(ya),
                            latex(xb),latex(yb),
                            latex(xa),latex(xb),latex(ya),latex(yb)
                        ))

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
            vdc_da_1_d = '\\True $\\left| %s \\vec{a}+%s\\vec{b} \\right|=%s$' %(latex(a),latex(c),latex(sqrt((a*xa+c*xb)**2+(a*ya+c*yb)**2)))
            vdc_da_1_s = '$\\left| %s \\vec{a}+%s\\vec{b} \\right|=%s$' %(latex(a),latex(c),latex(sqrt((a*xa+c*xb)**2+(a*ya+c*yb)**2+1)))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Độ dài vectơ $\\vec{v}=(%s x+%s; %s x+%s)$ bằng $%s$ khi $x=%s$ và $x=%s$' %(latex(a),latex(b),latex(c),latex(d),latex(h),latex(x0),latex(x1))
            vdc_da_2_s = 'Độ dài vectơ $\\vec{v}=(%s x+%s; %s x+%s)$ bằng $%s$ khi $x=%s$ và $x=%s$' %(latex(a),latex(b),latex(c),latex(d),latex(h),latex(x0+1),latex(x1))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1,vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\vec{a}=(%s; %s)$ suy ra $%s \\vec{a}=(%s; %s)$. \\\\ \n'
                            '\\hspace*{1cm} $\\vec{b}=(%s; %s)$ suy ra $%s \\vec{b}=(%s; %s)$. \\\\ \n'
                            '\\hspace*{1cm} $%s \\vec{a}+%s\\vec{b}=(%s; %s)$.\\\\ \n' 
                            'Vậy $\\left| %s \\vec{a}+%s\\vec{b} \\right|=\\sqrt{(%s)^2+(%s)^2}=%s$.'
                            %(latex(xa),latex(ya),latex(a),latex(a*xa),latex(a*ya),
                            latex(xb),latex(yb),latex(c),latex(c*xb),latex(c*yb),
                            latex(a),latex(c),latex(a*xa+c*xb),latex(a*ya+c*yb),
                            latex(a),latex(c),latex(a*xa+c*xb),latex(a*ya+c*yb),latex(sqrt((a*xa+c*xb)**2+(a*ya+c*yb)**2))
                        ))

            loigiai_vdc_2 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $\\left| \\vec{v} \\right|=%s \\Leftrightarrow  \\sqrt{(%s x+%s)^2+(%s x+%s)^2}=%s \\Leftrightarrow %s=0$. \\\\ \n'
                            'Giải phương trình ta được nghiệm $x=%s$ và $x=%s$.'
                            %(latex(h),latex(a),latex(b),latex(c),latex(d),latex(h),latex(pt),
                            latex(x0),latex(x1)
                        ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2]

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')
            return content

