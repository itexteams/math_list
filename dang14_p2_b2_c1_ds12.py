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


def bt_dang14_p2_b2_c1_ds12(self):
            # Khai báo biến
            x=symbols('x')
            #a=480
            #b=30
            #v=10
            #x0=(Rational(a,2*k))**(1/3)
            v=randint(10,15)
            i=randint(1,2)
            x0=i*v
            b=v*randint(1,2)
            a=b*v*Rational(2*b*x0**3,v**3)

            k=Rational(b,v**3)
            kqc=Rational(a,b)+k*b**2

            # Nội dung câu hỏi
            noidungcauhoi = ('''Chi phí nhiên liệu của một chiếc tàu chạy trên sông được chia thành hai phần. Phần thứ nhất không phụ thuộc vào vận tốc và bằng $%s$ nghìn đồng/giờ. Phần thứ hai tỉ lệ thuận với lập phương của vận tốc, khi $v=%s$ km/h thì phần thứ hai bằng $%s$ nghìn đồng/giờ'''                 
                             %(latex(a),latex(v),latex(b)
                                 ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Khi vận tốc $v=%s$ km/h thì chi phí nguyên liệu cho phần thứ nhất trên $1$ km đường sông là $%s$ nghìn đồng' %(latex(v),latex(Rational(1,v)*a*1000))
            nb_da_1_s = 'Khi vận tốc $v=%s$ km/h thì chi phí nguyên liệu cho phần thứ nhất trên $1$ km đường sông là $%s$ đồng' %(latex(v),latex(Rational(1,v)*(a-v*100)*1000))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Thời gian tàu chạy quãng đường $1$ km là $%s$ (giờ). \\\\
                            Chi phí tiền nhiên liệu cho phần thứ nhất là $%s \\cdot %s =%s$ (nghìn đồng).'''
                        %(latex(Rational(1,v)),
                          latex(Rational(1,v)),latex(a*1000),latex(Rational(1,v)*a*1000),
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
            th_da_1_d = '\\True Hàm số xác định tổng chi phí nguyên liệu trên $1$ km đường sông với vận tốc $x$ km/h là $f(x)=\\frac{%s}{x}+%s x^2$' %(latex(a),latex(k))
            th_da_1_s = 'Hàm số xác định tổng chi phí nguyên liệu trên $1$ km đường sông với vận tốc $x$ km/h là $f(x)=\\frac{%s}{x}+%s x^2$' %(latex(a+100),latex(k))  
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Gọi $x$ (km/h) là vận tốc của tàu, $x>0$. \\\\
                            Thời gian tàu chạy quãng đường $1$ km là $\\frac{1}{x}$ (giờ). \\\\
                                Chi phí tiền nhiên liệu cho phần thứ nhất là $\\frac{1}{x} \\cdot %s=\\frac{%s}{x}$ (nghìn đồng). \\\\
                                    Hàm chi phí cho phần thứ hai là $kx^3$ (nghìn đồng/giờ). \\\\
                            Mà khi $x=%s$ thì $p=%s$, suy ra $k=%s$. \\\\
                            Ta có $p=%s x^3$ (nghìn đồng/giờ). \\\\
                                Do đó chi phí để phần hai chạy $1$ km là $\\frac{1}{x} \\cdot %s x^3=%s x^2$ (nghìn đồng). \\\\
                            Vậy tổng chi phí là $f(x)=\\frac{%s}{x}+%s x^2$. '''       
                        %(latex(a),latex(a),
                          latex(v),latex(b),latex(Rational(b,v**3)),
                          latex(k),
                          latex(k),latex(k),
                          latex(a),latex(k)
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
            vd_da_1_d = '\\True Khi vận tốc $v=%s$ km/h thì tổng chi phí nguyên liệu trên $1$ km đường sông là $%s$ đồng'%(latex(v),latex(kqc*1000))
            vd_da_1_s = 'Khi vận tốc $v=%s$ km/h thì tổng chi phí nguyên liệu trên $1$ km đường sông là $%s$ đồng'%(latex(v),latex((kqc+1)*1000))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Tổng chi phí là $f(x)=\\frac{%s}{x}+%s x^2$. \\\\
                            Thay $x=v=%s$ (km/h) vào ta có $f(%s)=\\frac{%s}{%s}+%s %s^2=%s$ (nghìn đồng). \\\\
                                Suy ra chi phí nguyên liệu là $%s$ đồng.'''  
                        %(latex(a),latex(k),
                          latex(b),latex(b),latex(a),latex(b),latex(k),latex(b),latex(kqc),
                          latex(kqc*1000)
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
            vdc_da_1_d = '\\True Vận tốc của tàu để tổng chi phí nguyên liệu trên $1$ km đường sông nhỏ nhất là $%s$ km/h' %(latex(x0))
            vdc_da_1_s = 'Vận tốc của tàu để tổng chi phí nguyên liệu trên $1$ km đường sông nhỏ nhất là $%s$ km/h' %(latex(x0+5))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $f'(x)=-\\frac{%s}{x^2}+%s x=\\frac{%s x^3-%s}{x^2}$. \\\\
                             $f'(x)=0 \\Leftrightarrow x=%s$. \\\\
                                 Bảng biến thiên \\\\
                                     \\begin{tikzpicture}
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$x$/0.7,$f'(x)$/0.7,$f(x)$/2.1}
            {$0$,$%s$,$+\\infty$}
            \\tkzTabLine{,-,0,+}
            \\tkzTabVar{+/,-/$f(%s)$,+/}
            \\end{tikzpicture} \\\\
                Vậy vận tốc của tàu để tổng chi phí nguyên liệu trên $1$ km đường sông nhỏ nhất là $%s$ km/h.'''
                        %(latex(a),latex(2*k),latex(2*k),latex(a),
                          latex(x0),
                          latex(x0),latex(x0),
                          latex(x0)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('.0$', '$').replace('.0)$', ')$')
            return content

