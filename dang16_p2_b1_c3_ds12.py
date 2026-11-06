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


def bt_dang16_p2_b1_c3_ds12(self):
            # Khai báo biến
            x=symbols('x')
            lis1=[0.1,0.2,0.3,0.4,0.5]
            a=random.choice(lis1)
            lis0=[150,180,210,240,270,300]
            b=random.choice(lis0)
            lis2=[-0.3,-0.1]
            c=random.choice(lis2)
            lis3=[100000, 150000, 200000]
            p0=random.choice(lis3)
            lis4=[300,350,400,450,250]
            t=random.choice(lis4)
            A=t-b
            C=p0-A/a-b/c

            t0=randint(10,13)
            e=2.71828182846
            p1=round((A/a)*e**(a*t0)+(b/c)*e**(c*t0)+C,0)

            lis5=[450,500,550,600]
            m=random.choice(lis5)
            lisn=[0.1,0.2,0.4,0.5]
            n=random.choice(lisn)

            t1=randint(3,6)

            t2=t0+t1
            p2=round((A/a)*e**(a*t2)+(b/c)*e**(c*t2)+C,0)

            C1=round(p2-(m/n)*e**(n*t1),0)

            g0=m/n+C1
            # Nội dung câu hỏi
            noidungcauhoi = ('''\\immini{Một quần thể vi khuẩn $(A)$ có số lượng cá thể là $P(t)$ sau $t$ phút quan sát được phát hiện thay đổi với tốc độ là $P'(t)=a e^{%s t}+%s e^{%s t}$ vi khuẩn/phút, $(a \\in \\mathbb{R})$zz Biết rằng lúc bắt đầu quan sát, quần thể có $%s$ vi khuẩn và đạt tốc độ tăng trưởng là $%s$ vi khuẩn/phútzz}
                            {
                                \\tdplotsetmaincoords{70}{110}
                                \\scalebox{0zz4}{
                                    \\begin{tikzpicture}[tdplot_main_coords@ scale=1]
                                        \\shade[ball color=green] (0@0@0) circle (2cm);
                                        \\foreach \\theta in {0@45@zzzzzz@360} {
                                            \\foreach \\phi in {30@60@90@120@150} {
                                                \\pgfmathsetmacro{\\x}{2zz1*sin(\\phi)*cos(\\theta)}
                                                \\pgfmathsetmacro{\\y}{2zz1*sin(\\phi)*sin(\\theta)}
                                                \\pgfmathsetmacro{\\z}{2zz1*cos(\\phi)}
                                                \\pgfmathsetmacro{\\xB}{2zz6*sin(\\phi)*cos(\\theta)}
                                                \\pgfmathsetmacro{\\yB}{2zz6*sin(\\phi)*sin(\\theta)}
                                                \\pgfmathsetmacro{\\zB}{2zz6*cos(\\phi)}
                                                \\draw[green@ ultra thick@ ->] (\\x@\\y@\\z) -- (\\xB@\\yB@\\zB);}}
                                \\end{tikzpicture}}
                                \\scalebox{0zz6}{
                                    \\begin{tikzpicture}[tdplot_main_coords@ scale=1]
                                        \\shade[ball color=red] (0@0@0) circle (2cm);
                                        \\foreach \\theta in {0@45@zzzzzz@360} {
                                            \\foreach \\phi in {30@60@90@120@150} {
                                                \\pgfmathsetmacro{\\x}{2zz1*sin(\\phi)*cos(\\theta)}
                                                \\pgfmathsetmacro{\\y}{2zz1*sin(\\phi)*sin(\\theta)}
                                                \\pgfmathsetmacro{\\z}{2zz1*cos(\\phi)}
                                                \\pgfmathsetmacro{\\xB}{2zz6*sin(\\phi)*cos(\\theta)}
                                                \\pgfmathsetmacro{\\yB}{2zz6*sin(\\phi)*sin(\\theta)}
                                                \\pgfmathsetmacro{\\zB}{2zz6*cos(\\phi)}
                                                \\draw[red@ ultra thick@ ->] (\\x@\\y@\\z) -- (\\xB@\\yB@\\zB);}}
                                \\end{tikzpicture}}
                                }'''                 
                            %(latex(a),latex(b),latex(c),latex(p0),latex(t)
                                ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $a=%s$' %(latex(A))
            nb_da_1_s = '$a=%s$' %(latex(t+b))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Tại thời điểm bắt đầu quan sát quần thể có tốc độ thay đổi là $%s$ vi khuẩn/phút nên ta có \\\\
                            $P'(0)=%s \\Leftrightarrow a e^{0}+%s e^{0}=%s \\Leftrightarrow a=%s$zz'''
                        %(latex(t),latex(t),
                        latex(b),latex(t),latex(A)
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
            th_da_1_d = '\\True $P(t)=%s e^{%s t}+%s e^{%s t}+%s$'%(latex(A/a),latex(a),latex(b/c),latex(c),latex(C))
            th_da_1_s = '$P(t)=%s e^{%s t}+%s e^{%s t}+%s$'%(latex(A/a),latex(a),latex(b/c),latex(c),latex(C-100))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có \\\\
                            $P(t)=\\int P'(t) \\text{d}t =\\int \\left( %s e^{%s t}+%s e^{%s t} \\right) \\text{d}t=%s e^{%s t}+%s e^{%s t}+C$zz \\\\
                            Tại thời điểm bắt đầu quan sát quần thể có số lương là $%s$ vi khuẩn nên \\\\
                            $P(0)=%s \\Leftrightarrow %s e^{0}+%s e^{0}+C=%s \\Leftrightarrow C=%s$zz \\\\
                            Suy ra $P(t)=%s e^{%s t}+%s e^{%s t}+%s$zz'''       
                        %(latex(A),latex(a),latex(b),latex(c),
                        latex(A/a),latex(a),latex(b/c),latex(c),
                        latex(p0),
                        latex(p0),
                        latex(A/a),latex(b/c),latex(p0),latex(C),
                        latex(A/a),latex(a),latex(b/c),latex(c),latex(C)
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
            vd_da_1_d = '\\True Sau $%s$ phút số lượng vi khuẩn trong quần thể là $%s$ (làm tròn kết quả đến hàng đơn vị)' %(latex(t0),latex(p1))
            vd_da_1_s = 'Sau $%s$ phút số lượng vi khuẩn trong quần thể là $%s$ (làm tròn kết quả đến hàng đơn vị)' %(latex(t0),latex(p1+1000))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Sau $%s$ phút số lượng vi khuẩn trong quần thể là \\\\
                            $P(%s)=%s e^{%s \\cdot %s}+%s e^{%s \\cdot %s}+%s \\approx %s$zz'''  
                        %(latex(t0),
                        latex(t0),latex(A/a),latex(a),latex(t0),latex(b/c),latex(c),latex(t0),latex(C), latex(p1)
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
            vdc_da_1_d = '\\True Sau $%s$ phút, một quần thể vi khuẩn $(B)$ có tốc độ tăng trưởng là $G\'(t)=%s e^{%s t}$ vi khuẩn/phút bắt đầu cạnh tranh nguồn thức ăn trực tiếp với quần thể $(A)$, một cá thể tại quần thể $(B)$ triệt tiêu một cá thể tại quần thể $(A)$. Sau $%s$ phút cạnh tranh quần thể $(A)$ bị tiêu diệt hoàn toàn. Số lượng vi khuẩn của quần thể $(B)$ ở thời điểm bắt đầu cạnh tranh là $%s$ con (làm tròn kết quả đến hàng đơn vị)' %(latex(t0),latex(m),latex(n),latex(t1),latex(g0))
            vdc_da_1_s = 'Sau $%s$ phút, một quần thể vi khuẩn $(B)$ có tốc độ tăng trưởng là $G\'(t)=%s e^{%s t}$ vi khuẩn/phút bắt đầu cạnh tranh nguồn thức ăn trực tiếp với quần thể $(A)$, một cá thể tại quần thể $(B)$ triệt tiêu một cá thể tại quần thể $(A)$. Sau $%s$ phút cạnh tranh quần thể $(A)$ bị tiêu diệt hoàn toàn. Số lượng vi khuẩn của quần thể $(B)$ ở thời điểm bắt đầu cạnh tranh là $%s$ con (làm tròn kết quả đến hàng đơn vị)' %(latex(t0),latex(m),latex(n),latex(t1),latex(g0+1000))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Số lượng vi khuẩn của quần thể $(A)$ sau $%s$ phút là \\\\
                            $P(%s)=%s e^{%s \\cdot %s}+%s e^{%s \\cdot %s}+%s \\approx %s$zz \\\\
                            Theo bài toán thì sau $%s$ xuất hiện, số lượng vi khuẩn ở quần thể $(B)$ sẽ là \\\\
                                $G(%s)=P(%s)=%s$zz \\\\
                            Ta có \\\\
                                $G(t)=\\int G'(t) \\text{d}t =\\int %s e^{%s t} \\text{d}t=%s e^{%s t}+C'$zz \\\\
                            Vì $G(%s)=%s$ nên $C' \\approx %s$zz \\\\
                            Suy ra $G(t)=%s e^{%s t}+%s$zz \\\\
                            Vậy số lượng vi khuẩn của quần thể $(B)$ từ khi bắt đầu là \\\\
                            $G(0)=%s e^{0}+%s \\approx %s$zz'''
                        %(latex(t2),
                        latex(t2),latex(A/a),latex(a),latex(t2),latex(b/c),latex(c),latex(t2),latex(C), latex(p2),
                        latex(t1),
                        latex(t1),latex(t2),latex(p2),
                        latex(m),latex(n),latex(m/n),latex(n),
                        latex(t1),latex(p2),latex(C1),
                        latex(m/n),latex(n),latex(C1),
                        latex(m/n),latex(C1),latex(g0)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-').replace('.', ',').replace('zz', '.').replace(',0', '').replace('@', ',')
            return content

