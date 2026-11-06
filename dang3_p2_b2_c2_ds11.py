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


def bt_dang3_p2_b2_c2_ds11(self):
            # Khai báo biến
            #Số hạng đầu
            u1=randint(-9,9)
            #Công sai
            d=randint(-9,9)
            while d==0:
                d=randint(-9,9)
            #Số hạng thứ n
            n=randint(2,50)
            un=u1+(n-1)*d

            n1=randint(2,50)
            while n1==n:
                n1=randint(2,50)
            un1=u1+(n1-1)*d

            n2=randint(2,50)
            while n2==n or n2==n1:
                n2=randint(2,50)
            un2=u1+(n2-1)*d

            n3=randint(2,50)
            while n3==n or n3==n1 or n3==n2:
                n3=randint(2,50)
            un3=u1+(n3-1)*d

            #Tổng m số hạng đầu
            m=randint(10,50)
            sm=m*u1+Rational(m*(m-1)*d,2)

            m1=randint(10,50)
            while m1==m:
                m1=randint(10,50)
            sm1=m1*u1+Rational(m1*(m1-1)*d,2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho cấp số cộng $(u_n)$ với $u_1=%s$ và $u_{%s}=%s$. \n'''
                            %(latex(u1),latex(n),latex(un)
                            ))
            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Công sai của cấp số cộng là $d=%s$' %(latex(d))
            nb_da_1_s = 'Công sai của cấp số cộng là $d=%s$' %(latex(d+1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $u_{%s}=u_1+(%s-1)d \\Leftrightarrow %s=%s+(%s-1)d \\Leftrightarrow d=%s$.\\\\ \n' 
                            'Vậy công sai của cấp số cộng là $d=%s$.'
                            %(latex(n),latex(n),latex(un),latex(u1),latex(n),latex(d),latex(d)
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
            th_da_1_d = '\\True Số $%s$ là số hạng thứ $%s$ của cấp số cộng' %(latex(un1),latex(n1))
            th_da_1_s = 'Số $%s$ là số hạng thứ $%s$ của cấp số cộng' %(latex(un1),latex(n1+1))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True Số hạng thứ $%s$ của cấp số cộng là $u_{%s}=%s$' %(latex(n3),latex(n3),latex(un3))
            th_da_2_s = 'Số hạng thứ $%s$ của cấp số cộng là $u_{%s}=%s$' %(latex(n3),latex(n3),latex(un3+1))
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1,th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Gọi $u_n=%s \\Leftrightarrow u_1+(n-1)d=%s \\Leftrightarrow %s+(n-1) \\cdot (%s)=%s \\Leftrightarrow n=%s$. \\\\ \n'
                            'Vậy số $%s$ là số hạng thứ $%s$ của cấp số cộng.'
                        %(latex(un1),latex(un1),latex(u1),latex(d),latex(un1),latex(n1),
                        latex(un1),latex(n1),
                            ))
            loigiai_th_2 = ('Số hạng thứ $%s$ của cấp số cộng là \\\\ \n'
                            '\\hspace*{1cm} $u_{%s}=u_1+(%s-1)d=%s+(%s-1) \\cdot (%s)=%s$.' 
                            %(latex(n3),latex(n3),latex(n3),latex(u1),latex(n3),latex(d),latex(un3)
                            ))
            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1,loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Tổng $%s$ số hạng đầu của cấp số cộng là $%s$' %(latex(m),latex(sm))
            vd_da_1_s = 'Tổng $%s$ số hạng đầu của cấp số cộng là $%s$' %(latex(m),latex(sm+1))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Tổng $%s$ số hạng đầu của cấp số cộng là \\\\ \n'
                            '\\hspace*{1cm} $S_{%s}=%s u_1 +\\dfrac{%s(%s-1)}{2}d =%s \\cdot (%s) +\\dfrac{%s(%s-1)}{2} \\cdot (%s)=%s$.'
                            %(latex(m),
                            latex(m),latex(m),latex(m),latex(m),latex(m),latex(u1),latex(m),latex(m),latex(d),latex(sm)
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
            vdc_da_1_d = '\\True Số $%s$ là tổng $%s$ số hạng đầu của cấp số cộng' %(latex(sm1),latex(m1))
            vdc_da_1_s = 'Số $%s$ là tổng $%s$ số hạng đầu của cấp số cộng' %(latex(sm1),latex(m1+1))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Gọi $S_n=%s \\Leftrightarrow n u_1+\\dfrac{n(n-1)}{2}d=%s \\Leftrightarrow %s n+\\dfrac{n(n-1)}{2} \\cdot (%s)=%s$. \\\\ \n'
                            'Giải phương trình ta được $n=%s$. \\\\ \n'
                            'Vậy số $%s$ là tổng $%s$ số hạng đầu của cấp số cộng.'
                            %(latex(sm1),latex(sm1),latex(u1),latex(d),latex(sm1),
                            latex(m1),
                            latex(sm1),latex(m1)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

