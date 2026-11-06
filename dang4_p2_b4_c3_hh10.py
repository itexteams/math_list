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


def bt_dang4_p2_b4_c3_hh10(self):
            # Khai báo biến
            x=symbols('x')
            y=symbols('y')
            a=randint(2,15)
            b=randint(2,16)
            c=sqrt(a**2+b**2)
            x0=randint(4,16)
            x1=randint(-1,10)


            while a>=b or c==b or x0<=a or x1>=a:
                x=symbols('x')
                y=symbols('y')
                a=randint(2,15)
                b=randint(2,16)
                c=sqrt(a**2+b**2)
                x0=randint(4,16)
                x1=randint(-1,10)

            y0b=Rational((x0**2*b**2-a**2*b**2),a**2)
            y1b=Rational((x1**2*b**2-a**2*b**2),a**2)
            y0=sqrt(y0b)
            k=Rational(b,a)

            # Nội dung câu hỏi
            noidungcauhoi = ('Cho hypebol $(H)$ có dạng $%s x^2 - %s y^2= %s$.'
                            %(latex(b**2),latex(a**2),latex((a*b)**2)))



            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Tiêu điểm $F_1(%s;0),F_2(%s;0)$'%(latex(-c),latex(c))
            nb_da_1_s = 'Tiêu điểm $F_1(%s;0),F_2(%s;0)$'%(latex(-b),latex(b))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Tiêu điểm $F_1(%s;0),F_2(%s;0)$'%(latex(-c),latex(c))
            nb_da_2_s = 'Tiêu điểm $F_1(%s;0),F_2(%s;0)$'%(latex(-a),latex(a))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]

            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Ta có $(H):%s x^2 - %s y^2= %s \\Leftrightarrow \\dfrac{x^2}{%s}-\\dfrac{y^2}{%s}=1$\\\\ \n'
                            'Do đó $a^2=%s \\Rightarrow a=%s;b^2=%s \\Rightarrow b=%s; c^2=a^2+b^2=%s+%s=%s\\Rightarrow c=%s$.\\\\ \n'
                            'Tiêu điểm $F_1(%s;0),F_2(%s;0)$.'
                            %(latex(b**2),latex(a**2),latex((a*b)**2),latex(a**2),latex(b**2),
                            latex(a**2),latex(a),latex(b**2),latex(b),latex(a**2),latex(b**2),latex(a**2+b**2),latex(c),
                            latex(-c),latex(c))
                        )
            loigiai_nb_2 =  ('Ta có $(H):%s x^2 - %s y^2= %s \\Leftrightarrow \\dfrac{x^2}{%s}-\\dfrac{y^2}{%s}=1$. \\\\ \n'
                            'Do đó $a^2=%s \\Rightarrow a=%s;b^2=%s \\Rightarrow b=%s; c^2=a^2+b^2=%s+%s=%s\\Rightarrow c=%s$.\\\\ \n'
                            'Tiêu điểm $F_1(%s;0),F_2(%s;0)$.'
                            %(latex(b**2),latex(a**2),latex((a*b)**2),latex(a**2),latex(b**2),
                            latex(a**2),latex(a),latex(b**2),latex(b),latex(a**2),latex(b**2),latex(a**2+b**2),latex(c),
                            latex(-c),latex(c))
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
            th_da_1_d = '\\True Tiêu cự bằng $%s$'%(latex(2*c))
            th_da_1_s = 'Tiêu cự bằng $%s$'%(latex(2*a))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True Tiêu cự bằng $%s$'%(latex(2*c))
            th_da_2_s = 'Tiêu cự bằng $%s$'%(latex(2*b))
            list_th_da_2=[th_da_2_d,th_da_2_s]

            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('$c=%s$ nên tiêu cự $F_1F_2=2c=2\\cdot %s =%s$.'
                            %(latex(c),latex(c),latex(2*c))
                        )
            loigiai_th_2 = ('$c=%s$ nên tiêu cự $F_1F_2=2c=2\\cdot %s =%s$.'
                            %(latex(c),latex(c),latex(2*c))
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
            vd_da_1_d = '\\True Có hai điểm thuộc $(H)$ có hoành độ $x=%s$ '%(latex(x0))
            vd_da_1_s = 'Có một điểm thuộc $(H)$ có hoành độ $x=%s$ '%(latex(x0))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Không có điểm nào thuộc $(H)$ có hoành độ $x=%s$ '%(latex(x1))
            vd_da_2_s = 'Có hai điểm thuộc $(H)$ có hoành độ $x=%s$ '%(latex(x1))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]

            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('Thay $x=%s$ vào $(H):\\dfrac{%s}{%s}-\\dfrac{y^2}{%s}=1\\Leftrightarrow y^2=%s\\Leftrightarrow y=\\pm %s$. \\\\ \n'
                            'Vậy $M_1(%s;%s),M_2(%s;%s)$.'
                            %(latex(x0),latex(x0**2),latex(a**2),latex(b**2),latex(y0b),latex(y0),latex(x0),latex(-y0),latex(x0),latex(y0),)
                        )
            loigiai_vd_2 = ('Thay $x=%s$ vào $(H):\\dfrac{%s}{%s}-\\dfrac{y^2}{%s}=1\\Leftrightarrow y^2=%s<0$, không tồn tại giá trị thực của $y$. \\\\ \n'
                            'Vậy không có điểm nào thuộc $(H)$ có hoành độ $x=%s$.'
                            %(latex(x1),latex(x1**2),latex(a**2),latex(b**2),latex(y1b),
                            latex(x1))
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
            vdc_da_1_d = '\\True Đường thẳng $(d):y=kx$ có điểm chung với $(H)$ khi và chỉ khi $%s<k<%s$. '%(latex(-k),latex(k))
            vdc_da_1_s = 'Đường thẳng $(d):y=kx$ có điểm chung với $(H)$ khi và chỉ khi $%s<k<%s$. '%(latex(-a),latex(a))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Đường thẳng $(d):y=kx$ có điểm chung với $(H)$ khi và chỉ khi $%s<k<%s$. '%(latex(-k),latex(k))
            vdc_da_2_s = 'Đường thẳng $(d):y=kx$ có điểm chung với $(H)$ khi và chỉ khi $%s<k<%s$. '%(latex(-b),latex(b))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Tọa độ giao điểm của hypebol $(H)$ và đường thẳng $(d):y=kx$ là nghiệm của hệ\\\\ \n'
                            '$\\heva{& y=kx\\\\& %s x^2-%s y^2=%s}\\Rightarrow %s x^2- %s k^2x^2=%s \\Leftrightarrow \\left(%s -%s k^2\\right)x^2-%s=0$  $(1)$.\\\\ \n'
                            'Đường thẳng $(d)$ cắt $(H)$ khi và chỉ khi phương trình $(1)$ có nghiệm\\\\ \n'
                            '$\\Leftrightarrow \\heva{& %s-%sk^2\\ne 0 \\\\& x^2=\\dfrac{%s}{%s-%sk^2}\\ge 0}\\Leftrightarrow %s-%sk^2>0 \\Leftrightarrow %s<k<%s$.'

                            %(latex(b**2),latex(a**2),latex(a**2*b**2),latex(b**2),latex(a**2),latex(a**2*b**2),latex(b**2),latex(a**2),latex(a**2*b**2),
                            latex(b**2),latex(a**2),latex(a**2*b**2),latex(b**2),latex(a**2),latex(b**2),latex(a**2),latex(-k),latex(k))
                        )
            loigiai_vdc_2 = ('Tọa độ giao điểm của hypebol $(H)$ và đường thẳng $(d):y=kx$ là nghiệm của hệ\\\\ \n'
                            '$\\heva{& y=kx\\\\& %s x^2-%s y^2=%s}\\Rightarrow %s x^2- %s k^2x^2=%s \\Leftrightarrow \\left(%s -%s k^2\\right)x^2-%s=0$  $(1)$.\\\\ \n'
                            'Đường thẳng $(d)$ cắt $(H)$ khi và chỉ khi phương trình $(1)$ có nghiệm\\\\ \n'
                            '$\\Leftrightarrow \\heva{& %s-%sk^2\\ne 0 \\\\& x^2=\\dfrac{%s}{%s-%sk^2}\\ge 0}\\Leftrightarrow %s-%sk^2>0 \\Leftrightarrow %s<k<%s$.'

                            %(latex(b**2),latex(a**2),latex(a**2*b**2),latex(b**2),latex(a**2),latex(a**2*b**2),latex(b**2),latex(a**2),latex(a**2*b**2),
                            latex(b**2),latex(a**2),latex(a**2*b**2),latex(b**2),latex(a**2),latex(b**2),latex(a**2),latex(-k),latex(k))
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('- +','-').replace('+ -', '-').replace('- -', '+')
            return content   

