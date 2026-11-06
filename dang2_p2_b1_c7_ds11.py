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


def bt_dang2_p2_b1_c7_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                t=symbols('t')
                t0=symbols('t_0')

                x0=randint(-11,-1)
                x1=randint(1,11)
                x2=Rational(x0+x1,2)

                d=randint(-9,29)
                e=randint(-9,9)

                a=randint(2,9)
                b=randint(1,9)

                c=randint(-9,29)
                d=randint(-9,29)
                e=randint(-9,9)
                while a**2-(x0+x1)*a+x0*x1<=0 or (x0+x1)/2<=0:
                    x0=randint(-9,-1)
                    x1=randint(1,9)
                    x2=Rational(x0+x1,2)

                    d=randint(-9,29)
                    e=randint(-9,9)

                    a=randint(2,9)
                    b=randint(1,9)
                    c=randint(-9,29)
                    d=randint(-9,29)
                    e=randint(-9,9)

                B=-x0-x1
                C=x0*x1
                D=d
                Fx=Rational(1,3)*t**3+Rational(B,2)*t**2+C*t+D
                Fx0=Rational(1,3)*t0**3+Rational(B,2)*t0**2+C*t0+D

                FtF0=t**2+t*t0+t0**2
                FtF01=Rational(B,2)
                fx=t**2+B*t+C
                fx0=t0**2+B*t0+C
                fxtf0=t+t0+B
                dhc2=2*t+B
                av0=2*x1+B
                va0=x2**2+B*x2+C

                va=a**2-(x0+x1)*a+C
                gb=2*b-(x0+x1)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Một vật chuyển động thẳng xác định bởi phương trình $S=s(t)=%s$ trong đó $t$ được tính bằng giây và $S$ được tính bằng mét.'''
                                %(latex(Fx),)
                                )

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Vận tốc tại thời điểm $t=%s$s là $%s$m/s'%(latex(a),latex(va),)
                nb_da_1_s = 'Vận tốc tại thời điểm $t=%s$s là $%s$m/s'%(latex(a),latex(va+2),)
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Vận tốc tại thời điểm $t=%s$s là $%s$m/s'%(latex(a),latex(va),)
                nb_da_2_s = 'Vận tốc tại thời điểm $t=%s$s là $%s$m/s'%(latex(a),latex(va+1),)
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]

                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = ('''Tại $t_0\\in \\mathbb{R}$, ta có.\\\\ \n'''
                                ''' $s(t)-s(t_0)=%s-\\left(%s\\right)$\\\\ \n'''
                                '''\\hspace*{2.17cm}$=(t-t_0)\\left[\\dfrac{1}{3}(%s)+%s(t+t_0)+%s\\right]$.\\\\ \n'''
                                ''' $\\underset{t\\to {t}_{0}}\\lim\\dfrac{s(t)-s(t_0)}{t-t_0}=\\underset{t\\to {t}_{0}}\\lim \\left[\\dfrac{1}{3}(%s)+%s(t+t_0)+%s\\right]=%s$\\\\ \n'''
                                '''Ta có, $v(t)=s'(t)=%s$, suy ra vận tốc tại thời điểm $t=%s$ là $v(%s)=%s$m/s. '''
                                %(latex(Fx),latex(Fx0),
                                latex(FtF0),latex(FtF01),latex(C),
                                latex(FtF0),latex(FtF01),latex(C),latex(fx0),
                                latex(fx),latex(a),latex(a),latex(va),
                                )                )
                loigiai_nb_2 = ('''Tại $t_0\\in \\mathbb{R}$, ta có.\\\\ \n'''
                                ''' $s(t)-s(t_0)=%s-\\left(%s\\right)$\\\\ \n'''
                                '''\\hspace*{2.17cm}$=(t-t_0)\\left[\\dfrac{1}{3}(%s)+%s(t+t_0)+%s\\right]$.\\\\ \n'''
                                ''' $\\underset{t\\to {t}_{0}}\\lim\\dfrac{s(t)-s(t_0)}{t-t_0}=\\underset{t\\to {t}_{0}}\\lim \\left[\\dfrac{1}{3}(%s)+%s(t+t_0)+%s\\right]=%s$\\\\ \n'''
                                '''Ta có, $v(t)=s'(t)=%s$, suy ra vận tốc tại thời điểm $t=%s$ là $v(%s)=%s$m/s. '''
                                %(latex(Fx),latex(Fx0),
                                latex(FtF0),latex(FtF01),latex(C),
                                latex(FtF0),latex(FtF01),latex(C),latex(fx0),
                                latex(fx),latex(a),latex(a),latex(va),
                                )                )
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
                th_da_1_d = '''\\True Gia tốc tại thời điểm $t=%s$s là $%s$m/s$^2$'''%(latex(b),latex(gb),)
                th_da_1_s = '''Gia tốc tại thời điểm $t=%s$s là $%s$m/s$^2$'''%(latex(b),latex(gb+2),)
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)
                th_da_2_d = '''\\True Gia tốc tại thời điểm $t=%s$s là $%s$m/s$^2$'''%(latex(b),latex(gb),)
                th_da_2_s = '''Gia tốc tại thời điểm $t=%s$s là $%s$m/s$^2$'''%(latex(b),latex(gb+1),)
                list_th_da_2=[th_da_2_d,th_da_2_s]
                th_da_2=random.choice(list_th_da_2)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1, th_da_2]
                # Nội dung lời giải
                loigiai_th_1 = ('''Tại $t_0\\in \\mathbb{R}$, ta có.\\\\ \n'''
                                ''' $v(t)-v(t_0)=%s-\\left(%s\\right)$\\\\ \n'''
                                '''\\hspace*{2.17cm}$=(t-t_0)(%s)$.\\\\ \n'''
                                ''' $\\underset{t\\to {t}_{0}}\\lim\\dfrac{v(t)-v(t_0)}{t-t_0}=\\underset{t\\to {t}_{0}}\\lim \\dfrac{(t-t_0)(%s)}{t-t_0}=\\underset{t\\to {t}_{0}}\\lim (%s)=2t_0+%s$\\\\ \n'''
                                '''Ta có, $a(t)=v'(t)=%s$, suy ra gia tốc tại thời điểm $t=%s$ là $a(%s)=%s$m/s$^2$. '''
                                %(latex(fx),latex(fx0),
                                latex(fxtf0),
                                latex(fxtf0),latex(fxtf0),latex(B),
                                latex(dhc2),latex(b),latex(b),latex(gb),
                                )                )
                loigiai_th_2 =('''Tại $t_0\\in \\mathbb{R}$, ta có.\\\\ \n'''
                                ''' $v(t)-v(t_0)=%s-\\left(%s\\right)$\\\\ \n'''
                                '''\\hspace*{2.17cm}$=(t-t_0)(%s)$.\\\\ \n'''
                                ''' $\\underset{t\\to {t}_{0}}\\lim\\dfrac{v(t)-v(t_0)}{t-t_0}=\\underset{t\\to {t}_{0}}\\lim \\dfrac{(t-t_0)(%s)}{t-t_0}=\\underset{t\\to {t}_{0}}\\lim (%s)=2t_0+%s$\\\\ \n'''
                                '''Ta có, $a(t)=v'(t)=%s$, suy ra gia tốc tại thời điểm $t=%s$ là $a(%s)=%s$m/s$^2$. '''
                                %(latex(fx),latex(fx0),
                                latex(fxtf0),
                                latex(fxtf0),latex(fxtf0),latex(B),
                                latex(dhc2),latex(b),latex(b),latex(gb),
                                )                )
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
                vd_da_1_d = '''\\True Gia tốc tại thời điểm vận tốc triệt tiêu là $%s$m/s$^2$ '''%(latex(av0))
                vd_da_1_s = '''Gia tốc tại thời điểm vận tốc triệt tiêu là $%s$m/s$^2$ '''%(latex(av0+1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '''\\True Gia tốc tại thời điểm vận tốc triệt tiêu là $%s$m/s$^2$ '''%(latex(av0))
                vd_da_2_s = ''' Gia tốc tại thời điểm vận tốc triệt tiêu là $%s$m/s$^2$ '''%(latex(av0-1))
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]

                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2]

                # Nội dung lời giải
                loigiai_vd_1 = ('''Khi vận tốc triệt tiêu ta có, $%s=0\\Leftrightarrow \\hoac{&t=%s\\\\& t=%s}$, với $t>0$ suy ra $t=%s$. \\\\ \n'''
                                '''Khi đó gia tốc là $a(%s)=%s$m/s$^2$. '''
                                %(latex(fx),latex(x0),latex(x1),latex(x1),
                                latex(x1),latex(av0),
                                )                )

                loigiai_vd_2 =  ('''Khi vận tốc triệt tiêu ta có, $%s=0\\Leftrightarrow \\hoac{&t=%s\\\\& t=%s}$, với $t>0$ suy ra $t=%s$. \\\\ \n'''
                                '''Khi đó gia tốc là $a(%s)=%s$m/s$^2$. '''
                                %(latex(fx),latex(x0),latex(x1),latex(x1),
                                latex(x1),latex(av0),
                                )                )

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
                vdc_da_1_d = '''\\True Vận tốc tại thời điểm gia tốc triệt tiêu là $%s$m/s '''%(latex(va0))
                vdc_da_1_s = '''Vận tốc tại thời điểm gia tốc triệt tiêu là $%s$m/s '''%(latex(va0+1))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '''\\True Vận tốc tại thời điểm gia tốc triệt tiêu là $%s$m/s '''%(latex(va0))
                vdc_da_2_s = '''Vận tốc tại thời điểm gia tốc triệt tiêu là $%s$m/s '''%(latex(va0-1))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 = ('''Khi gia tốc triệt tiêu ta có, $%s=0\\Leftrightarrow t=%s$. \\\\ \n'''
                                '''Khi đó vận tốc là $v\\left(%s\\right)=%s$m/s. '''
                                %(latex(dhc2),latex(x2),
                                latex(x2),latex(va0),
                                )
                            )
                loigiai_vdc_2 = ('''Khi gia tốc triệt tiêu ta có, $%s=0\\Leftrightarrow t=%s$. \\\\ \n'''
                                '''Khi đó vận tốc là $v\\left(%s\\right)=%s$m/s. '''
                                %(latex(dhc2),latex(x2),
                                latex(x2),latex(va0),
                                )
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

