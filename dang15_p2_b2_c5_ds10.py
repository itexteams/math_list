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


def bt_dang15_p2_b2_c5_ds10(self):
            # Khai báo biến
            # Khai báo biến
            a=randint(4,10)
            b=randint(4,12)
            while a==b:
                a=randint(4,10)
                b=randint(4,12)
            s=a+b
            n0=math.comb(s, 3)
            n2=math.comb(a, 3)
            n22=math.comb(b, 3)
            p2=Rational(n2,n0)
            p22=Rational(n22,n0)
            n3=math.comb(a, 2)*math.comb(b, 1)
            n33=math.comb(a, 1)*math.comb(b, 2)
            p3=Rational(n3,n0)
            p33=Rational(n33,n0)
            n4=n0-n22
            n44=n0-n2
            p4=Rational(n4,n0)
            p44=Rational(n44,n0)
            lisdm1=['đỏ','vàng','xanh']
            m1=random.choice(lisdm1)
            lisdm2=['đen','tím','cam']
            m2=random.choice(lisdm2)


            # Nội dung câu hỏi
            noidungcauhoi = ('''Một hộp có chứa $%s$ viên bi trong đó có $%s$ viên bi màu %s và $%s$ màu %s. Chọn ngẫu nhiên $3$ viên bi từ hộp đó.'''                 
                             %(latex(s),latex(a),m1,latex(b),m2
                                 ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Số phần tử không gian mẫu của phép thử là $n(\\Omega)=%s$'%(latex(n0))
            nb_da_1_s = 'Số phần tử không gian mẫu của phép thử là $n(\\Omega)=%s$'%(latex(s))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Số phần tử không gian mẫu của phép thử là $n(\\Omega)=C_{%s}^3=%s$.'%(latex(s),latex(n0))
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
            th_da_1_d = '\\True Xác suất để chọn được ba viên bi màu %s là $%s$' %(m1,latex(p2))  
            th_da_1_s = 'Xác suất để chọn được ba viên bi màu %s là $%s$' %(m1,latex(p22))   
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True Xác suất để chọn được ba viên bi màu %s là $%s$' %(m2,latex(p22))  
            th_da_2_s = 'Xác suất để chọn được ba viên bi màu %s là $%s$' %(m2,latex(p2))   
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1,th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Gọi $A$ là biến cố "Chọn được $3$ màu %s".\\\\ \n'
                            'Số cách chọn được $3$ viên bi màu %s là $n(A)=C_{%s}^3=%s$.\\\\ \n'
                            'Xác suất của biến cố $A$ là $P(A)=\\dfrac{n(A)}{n(\\Omega)}=%s$.'  
                        %(m1,m1,latex(a),latex(n2),latex(p2)
                            ))

            loigiai_th_2 =  ('Gọi $A$ là biến cố "Chọn được $3$ màu %s".\\\\ \n'
                            'Số cách chọn được $3$ viên bi màu %s là $n(A)=C_{%s}^3=%s$.\\\\ \n'
                            'Xác suất của biến cố $A$ là $P(A)=\\dfrac{n(A)}{n(\\Omega)}=%s$.'  
                        %(m2,m2,latex(b),latex(n22),latex(p22)
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
            vd_da_1_d = '\\True Xác suất để chọn được hai viên bi màu %s và một viên bi màu %s là $%s$' %(m1,m2,latex(p3))  
            vd_da_1_s = 'Xác suất để chọn được hai viên bi màu %s và một viên bi màu %s là $%s$' %(m1,m2,latex(p33))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Xác suất để chọn được một viên bi màu %s và hai viên bi màu %s là $%s$' %(m1,m2,latex(p33))  
            vd_da_2_s = 'Xác suất để chọn được một viên bi màu %s và hai viên bi màu %s là $%s$' %(m1,m2,latex(p3))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1,vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 =('Gọi $B$ là biến cố "Chọn được hai viên bi màu %s và một viên bi màu %s".\\\\ \n'
                           'Số cách chọn được hai viên bi màu %s và một viên bi màu %s là $n(B)=C_{%s}^2\\cdot C_{%s}^1=%s$.\\\\ \n'
                           'Xác suất của biến cố $B$ là $P(B)=\\dfrac{n(B)}{n(\\Omega)}=%s$.'  
                        %(m1,m2,m1,m2,latex(a),latex(b),latex(n3),latex(p3)
                            ))

            loigiai_vd_2 =('Gọi $B$ là biến cố "Chọn được một viên bi màu %s và hai viên bi màu %s".\\\\ \n'
                           'Số cách chọn được một viên bi màu %s và hai viên bi màu %s là $n(B)=C_{%s}^2\\cdot C_{%s}^1=%s$.\\\\ \n'
                           'Xác suất của biến cố $B$ là $P(B)=\\dfrac{n(B)}{n(\\Omega)}=%s$.'  
                        %(m1,m2,m1,m2,latex(a),latex(b),latex(n33),latex(p33)
                            ))
            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1,loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Xác suất để ba viên bi được chọn có ít nhất một viên bi màu %s là $%s$' %(m1,latex(p4)) 
            vdc_da_1_s = 'Xác suất để ba viên bi được chọn có ít nhất một viên bi màu %s là $%s$' %(m1,latex(p44))  
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Xác suất để ba viên bi được chọn có ít nhất một viên bi màu %s là $%s$' %(m2,latex(p44)) 
            vdc_da_2_s = 'Xác suất để ba viên bi được chọn có ít nhất một viên bi màu %s là $%s$' %(m2,latex(p4))  
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1,vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Gọi $C$ là biến cố "Ba viên bi được chọn có ít nhất một viên bi màu %s".\\\\ \n'
                             'Biến cố đối $\\overline{C}$ là biến cố "Cả ba viên bi được chọn có màu %s"\\\\ \n'
                           'Số phần tử của biến cố đối là $n(\\overline{C})=C_{%s}^3=%s$.\\\\ \n'
                           'Xác suất của biến cố đối là $P(\\overline{C})=\\dfrac{n(\\overline{C})}{n(\\Omega)}=%s$.\\\\ \n'
                           'Xác suất của biến cố $C$ là $P(C)=1-P(\\overline{C})=1-%s=%s$.'
                        %(m1,m2,latex(b),latex(n22),latex(p22),latex(p22),latex(p4)
                            ))

            loigiai_vdc_2 = ('Gọi $C$ là biến cố "Ba viên bi được chọn có ít nhất một viên bi màu %s".\\\\ \n'
                             'Biến cố đối $\\overline{C}$ là biến cố "Cả ba viên bi được chọn có màu %s"\\\\ \n'
                           'Số phần tử của biến cố đối là $n(\\overline{C})=C_{%s}^3=%s$.\\\\ \n'
                           'Xác suất của biến cố đối là $P(\\overline{C})=\\dfrac{n(\\overline{C})}{n(\\Omega)}=%s$.\\\\ \n'
                           'Xác suất của biến cố $C$ là $P(C)=1-P(\\overline{C})=1-%s=%s$.'
                        %(m2,m1,latex(a),latex(n2),latex(p2),latex(p2),latex(p44)
                            ))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

