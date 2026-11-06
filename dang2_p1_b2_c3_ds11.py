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


def bt_dang2_p1_b2_c3_ds11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
            dang=random.choice(lisdang)

            if dang=='20':
                # Khai báo biến
                lisv=[5,10,15,20,25,30]
                v=random.choice(lisv)
                xe1 = randint(1, 10)
                xe2 = randint(1, 10)
                xe3 = randint(1, 10)
                xe4 = randint(1, 10)
                xe5 = randint(1, 10)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[2,4,6,8,10]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Một phòng khám thống kê số bệnh nhân đến khám bệnh trong các ngày được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Số bệnh nhân & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số ngày & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại điện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='19':
                # Khai báo biến
                lisv=[0.5,1,1.5,2,2.5,3]
                v=random.choice(lisv)
                xe1 = randint(1, 10)
                xe2 = randint(1, 10)
                xe3 = randint(1, 10)
                xe4 = randint(1, 10)
                xe5 = randint(1, 10)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[1,2,3,4,5,6]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Kiểm tra điện lượng (nghìn mAh) của các viên pin tiểu do một hãng sản xuất được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Điện lượng (nghìn mAh) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số viên pin & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='18':
                # Khai báo biến
                lisv=[2,4,6,8,10]
                v=random.choice(lisv)
                xe1 = randint(1, 10)
                xe2 = randint(1, 10)
                xe3 = randint(1, 10)
                xe4 = randint(1, 10)
                xe5 = randint(1, 10)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[1,2,3,4,5,6]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Một hãng xe ô tô thống kê lại số lần gặp sự cố về động cơ của những chiếc xe cùng loại sau một thời gian sử dụng được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Số lần gặp sự cố & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số xe & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='17':
                # Khai báo biến
                lisv=[2,4,6,8,10]
                v=random.choice(lisv)
                xe1 = randint(1, 10)
                xe2 = randint(1, 10)
                xe3 = randint(1, 10)
                xe4 = randint(1, 10)
                xe5 = randint(1, 10)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[2,4,6,8,10]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Kết quả điều tra về số giờ làm thêm (giờ) của các công nhân tại một nhà máy được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Số giờ (giờ) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số công nhân & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='16':
                # Khai báo biến
                lisv=[60,65,70,75,80,85]
                v=random.choice(lisv)
                xe1 = randint(1, 10)
                xe2 = randint(1, 10)
                xe3 = randint(1, 10)
                xe4 = randint(1, 10)
                xe5 = randint(1, 10)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[5,10,15,20]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Người ta thống kê tốc độ (km/h) của xe ô tô di chuyển qua một trạm kiểm soát trên đường cao tốc được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Tốc độ (km/h) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số xe & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='15':
                # Khai báo biến
                lisv=[3,4,5,6,7,8]
                v=random.choice(lisv)
                xe1 = randint(1, 10)
                xe2 = randint(1, 10)
                xe3 = randint(1, 10)
                xe4 = randint(1, 10)
                xe5 = randint(1, 10)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[1,2,3,4,5,6]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Lượng nước sạch tiêu thụ (m$^3$) của các hộ gia đình được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Lượng nước (m$^3$) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số hộ gia đình & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='14':
                # Khai báo biến
                lisv=[50,55,60,65,70,75,80]
                v=random.choice(lisv)
                xe1 = randint(1, 10)
                xe2 = randint(1, 10)
                xe3 = randint(1, 10)
                xe4 = randint(1, 10)
                xe5 = randint(1, 10)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[2,4,6,8]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Khối lượng (gam) của các quả măng cụt trong một cửa hàng được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Khối lượng (gam) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số quả & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='13':
                # Khai báo biến
                lisv=[2,3,4,5,6,7,8]
                v=random.choice(lisv)
                xe1 = randint(1, 10)
                xe2 = randint(1, 10)
                xe3 = randint(1, 10)
                xe4 = randint(1, 10)
                xe5 = randint(1, 10)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[1,2,3,4,5]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Chiều cao (m) của các cây dừa tại một vườn cây trái ở Bến Tre được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Chiều cao (m) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số cây & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='12':
                # Khai báo biến
                lisv=[15,20,25,30,35,40]
                v=random.choice(lisv)
                xe1 = randint(1, 10)
                xe2 = randint(1, 10)
                xe3 = randint(1, 10)
                xe4 = randint(1, 10)
                xe5 = randint(1, 10)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[5,10,15,20]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Thời gian chạy bộ (phút) trong các ngày của một người được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Thời gian (phút) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số ngày & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='11':
                # Khai báo biến
                lisv=[1,2,3,4,5,6,7,8,9,10]
                v=random.choice(lisv)
                xe1 = randint(1, 10)
                xe2 = randint(1, 10)
                xe3 = randint(1, 10)
                xe4 = randint(1, 10)
                xe5 = randint(1, 10)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[5,10,15,20]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Thời gian đàm thoại (phút) của các cuộc gọi được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Thời gian (phút) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số cuộc gọi & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='10':
                # Khai báo biến
                lisv=[2,3,4,5,6,7,8,9,10]
                v=random.choice(lisv)
                xe1=randint(10,50)
                xe2=randint(10,50)
                xe3=randint(10,50)
                xe4=randint(10,50)
                xe5=randint(10,50)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[5,10,15,20]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Mức thưởng tết (triệu đồng) cho các nhân viên của một công ty được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Mức thưởng (triệu đồng) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số nhân viên & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='9':
                # Khai báo biến
                lisv=[60,65,70,75,80,85]
                v=random.choice(lisv)
                xe1=randint(10,50)
                xe2=randint(10,50)
                xe3=randint(10,50)
                xe4=randint(10,50)
                xe5=randint(10,50)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[5,10,15,20]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Thời gian (phút) hoàn thành giải chạy của các vận động viên được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Thời gian (phút) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số vận động viên & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='8':
                # Khai báo biến
                lisv=[150,155,160,165,170,175]
                v=random.choice(lisv)
                xe1=randint(10,50)
                xe2=randint(10,50)
                xe3=randint(10,50)
                xe4=randint(10,50)
                xe5=randint(10,50)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[5,10,15,20]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Thành tích nhảy xa (centimet) của các học sinh được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Thành tích (cm) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số học sinh & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='7':
                # Khai báo biến
                lisv=[45,50,55,60,65]
                v=random.choice(lisv)
                xe1=randint(10,50)
                xe2=randint(10,50)
                xe3=randint(10,50)
                xe4=randint(10,50)
                xe5=randint(10,50)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[5,10,15,20]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Thời gian sử dụng Internet hàng ngày của một số người được cho trong bảng số liệu sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Thời gian (phút) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số người & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$.'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))
            if dang=='6':
                # Khai báo biến
                lisv=[50,55,60,65,70,75,80,85]
                v=random.choice(lisv)
                xe1=randint(5,10)
                xe2=randint(5,10)
                xe3=randint(5,10)
                xe4=randint(5,10)
                xe5=randint(5,10)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[5,10,15,20,25]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Số tiền (đơn vị: nghìn đồng) mà khách hàng mua sách trong một ngày ở một cửa hàng sách được cho trong bảng sau \n'

                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|} \n'
                                '\\hline \n'
                                'Số tiền (nghìn đồng) & Số khách hàng \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s, %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '& $n=%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'

                                %(
                                latex(v),latex(v+k),latex(xe1),
                                latex(v+k),latex(v+2*k),latex(xe2),
                                latex(v+2*k),latex(v+3*k),latex(xe3),
                                latex(v+3*k),latex(v+4*k),latex(xe4),
                                latex(v+4*k),latex(v+5*k),latex(xe5),
                                latex(tong),


                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='5':
                # Khai báo biến
                lisv=[20,25,30,35,40]
                v=random.choice(lisv)
                xe1=randint(5,10)
                xe2=randint(5,10)
                xe3=randint(5,10)
                xe4=randint(5,10)
                xe5=randint(5,10)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[1,2,3,4]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Chiều cao (đơn vị: centimet) của các mẫu cây ở một vườn thực vật được cho trong bảng sau \n'

                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|} \n'
                                '\\hline \n'
                                'Chiều cao (cm) & Số cây \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s, %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '& $n=%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'

                                %(
                                latex(v),latex(v+k),latex(xe1),
                                latex(v+k),latex(v+2*k),latex(xe2),
                                latex(v+2*k),latex(v+3*k),latex(xe3),
                                latex(v+3*k),latex(v+4*k),latex(xe4),
                                latex(v+4*k),latex(v+5*k),latex(xe5),
                                latex(tong),


                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='4':
                # Khai báo biến
                lisv=[150,155,160,165]
                v=random.choice(lisv)
                xe1=randint(5,10)
                xe2=randint(5,10)
                xe3=randint(5,10)
                xe4=randint(5,10)
                xe5=randint(5,10)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[1,2,3,4]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Chiều cao (đơn vị: centimet) của các học sinh lớp 11B được cho trong bảng sau \n'

                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|} \n'
                                '\\hline \n'
                                'Chiều cao (cm) & Số học sinh \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s, %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '& $n=%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'

                                %(
                                latex(v),latex(v+k),latex(xe1),
                                latex(v+k),latex(v+2*k),latex(xe2),
                                latex(v+2*k),latex(v+3*k),latex(xe3),
                                latex(v+3*k),latex(v+4*k),latex(xe4),
                                latex(v+4*k),latex(v+5*k),latex(xe5),
                                latex(tong),


                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='3':
                # Khai báo biến
                lisv=[45,50,55,60,65]
                v=random.choice(lisv)
                xe1=randint(10,50)
                xe2=randint(10,50)
                xe3=randint(10,50)
                xe4=randint(10,50)
                xe5=randint(10,50)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[5,10,15,20]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Năng suất lúa (đơn vị: tạ/ha) của các địa phương được cho trong bảng sau \n'

                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|} \n'
                                '\\hline \n'
                                'Năng suất (tạ/ha) & Số địa phương \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s, %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '$[%s; %s)$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '& $n=%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'

                                %(
                                latex(v),latex(v+k),latex(xe1),
                                latex(v+k),latex(v+2*k),latex(xe2),
                                latex(v+2*k),latex(v+3*k),latex(xe3),
                                latex(v+3*k),latex(v+4*k),latex(xe4),
                                latex(v+4*k),latex(v+5*k),latex(xe5),
                                latex(tong),


                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            if dang=='2':
                # Khai báo biến
                lisv=[45,50,55,60,65]
                v=random.choice(lisv)
                xe1=randint(10,50)
                xe2=randint(10,50)
                xe3=randint(10,50)
                xe4=randint(10,50)
                xe5=randint(10,50)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[5,10,15,20]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)

                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Thời gian hoàn thành bài kiểm tra của các bạn trong lớp $11$B được cho trong bảng sau \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|}  \n'
                                '\\hline \n'
                                'Thời gian (phút) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số học sinh & $%s$ & $%s$ & $%s$ & $%s$ & $%s$\\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))
            if dang=='1':
                # Khai báo biến
                lisv=[45,50,55,60,65]
                v=random.choice(lisv)
                xe1=randint(10,50)
                xe2=randint(10,50)
                xe3=randint(10,50)
                xe4=randint(10,50)
                xe5=randint(10,50)
                tong=xe1+xe2+xe3+xe4+xe5

                lisk=[5,10,15,20]
                k=random.choice(lisk)

                x1=Rational(v+v+k,2)
                x2=Rational(v+k+v+2*k,2)
                x3=Rational(v+2*k+v+3*k,2)
                x4=Rational(v+3*k+v+4*k,2)
                x5=Rational(v+4*k+v+5*k,2)

                xtb=Rational(xe1*x1+xe2*x2+xe3*x3+xe4*x4+xe5*x5,tong)


                du = ['$\\bar{x}=%s$'%(latex(xtb)),
                    ]
                da= random.choice(du)
                s = ['$\\bar{x}=%s$'%(latex(xtb+1)),
                    '$\\bar{x}=%s$'%(latex(xtb+2)),
                    '$\\bar{x}=%s$'%(latex(xtb+3)),
                    '$\\bar{x}=%s$'%(latex(xtb-1)),
                    '$\\bar{x}=%s$'%(latex(xtb-2)),
                    '$\\bar{x}=%s$'%(latex(xtb-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Dữ liệu về tốc độ của các xe ô tô lưu thông trên một đoạn đường được trích xuất từ camera của cơ quan cảnh sát giao thông được cho trong bảng số liệu sau \\\\ \n'
                                '\\begin{center} \n'
                                '\\begin{tabular}{|c|c|c|c|c|c|} \n'
                                '\\hline \n'
                                'Tốc độ (km/h) & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ & $[%s; %s)$ \\\\ \n'
                                '\\hline \n'
                                'Số xe & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
                                '\\hline \n'
                                '\\end{tabular} \n'
                                '\\end{center} \n'
                                'Số trung bình của mẫu số liệu là'
                                %(
                                latex(v),latex(v+k),latex(v+k),latex(v+2*k),latex(v+2*k),latex(v+3*k),latex(v+3*k),latex(v+4*k),latex(v+4*k),latex(v+5*k),
                                latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),

                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Cỡ mẫu là $n=%s+%s+%s+%s+%s=%s$. \\\\ \n'
                        'Giá trị đại diện của các nhóm là \\\\ \n'
                        '\\hspace*{1cm} $x_1=%s, x_2=%s, x_3=%s, x_4=%s, x_5=%s$. \\\\ \n'
                        'Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s}=%s$. \\\\ \n'
                        %(latex(xe1),latex(xe2),latex(xe3),latex(xe4),latex(xe5),latex(tong),
                            latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                        latex(xe1),latex(x1),latex(xe2),latex(x2),latex(xe3),latex(x3),latex(xe4),latex(x4),latex(xe5),latex(x5),latex(tong),latex(xtb)

                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

