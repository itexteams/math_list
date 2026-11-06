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


def bt_dang20_p1_b1_c1_ds12(self):
            # Khai báo biến
            x1=randint(-9,9)
            i=randint(1,5)
            x2=x1+i
            j=randint(1,5)
            x3=x2+j

            y1=randint(-20,20)
            y2=randint(-20,20)

            lisdang=['1','2','3','4','5','6','7','8','1','1','1','1']
            dang=random.choice(lisdang)
            if dang=='8':
                d = ['$2$',
                    ]
                da= random.choice(d)
                s = ['$0$',
                    '$1$',
                    '$3$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:  \\\\ \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture}  \n'
                                    '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1}  \n'
                                    '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                                    '\\tkzTabLine{,+,0,-,d,-,0,+,}  \n'
                                    '\\tkzTabVar{-/$-\\infty$,+/$%s$,-D+/$-\\infty$/$+\\infty$,-/$%s$,+/$+\\infty$}  \n'
                                '\\end{tikzpicture}  \n'
                                '\\end{center} \n'
                                'Số điểm cực trị của hàm số là'
                                %(latex(x1),latex(x2),latex(x3),
                                latex(y1),latex(y2)
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
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Số điểm cực trị của hàm số là $2$. \\\\ \n'
                        )
            if dang=='7':
                d = ['$(%s;%s)$'%(latex(x3),latex(y2)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(x1)),
                    '$x=%s$'%(latex(y1)),
                    '$x=%s$'%(latex(y2)),
                    '$y=%s$'%(latex(x3)),
                    '$y=%s$'%(latex(y2)),
                    '$x=%s$'%(latex(x3)),
                    '$y=%s$'%(latex(x1)),
                    '$y=%s$'%(latex(y1)),
                    '$(%s;%s)$'%(latex(x1),latex(y1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:  \\\\ \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture}   \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,-,0,+,d,+,0,-,}  \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-/$-\\infty$}  \n'
                                '\\end{tikzpicture}  \n'
                                '\\end{center} \n'
                                'Điểm cực đại của đồ thị hàm số là'
                                %(latex(x1),latex(x2),latex(x3),
                                latex(y1),latex(y2)
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
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Điểm cực đại của đồ thị hàm số là $(%s;%s)$. \\\\ \n'
                        %(latex(x3),latex(y2),
                        ))
            if dang=='6':
                d = ['$(%s;%s)$'%(latex(x1),latex(y1)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(x1)),
                    '$x=%s$'%(latex(y1)),
                    '$x=%s$'%(latex(y2)),
                    '$y=%s$'%(latex(x3)),
                    '$y=%s$'%(latex(y2)),
                    '$x=%s$'%(latex(x3)),
                    '$y=%s$'%(latex(x1)),
                    '$y=%s$'%(latex(y1)),
                    '$(%s;%s)$'%(latex(x3),latex(y2)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:  \\\\ \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture}   \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,-,0,+,d,+,0,-,}  \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-/$-\\infty$}  \n'
                                '\\end{tikzpicture}  \n'
                                '\\end{center} \n'
                                'Điểm cực tiểu của đồ thị hàm số là'
                                %(latex(x1),latex(x2),latex(x3),
                                latex(y1),latex(y2)
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
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Điểm cực tiểu của đồ thị hàm số là $(%s;%s)$. \\\\ \n'
                        %(latex(x1),latex(y1),
                        ))
            if dang=='5':
                d = ['$y=%s$'%(latex(y1)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(x1)),
                    '$x=%s$'%(latex(y1)),
                    '$x=%s$'%(latex(y2)),
                    '$y=%s$'%(latex(x3)),
                    '$y=%s$'%(latex(y2)),
                    '$x=%s$'%(latex(x3)),
                    '$y=%s$'%(latex(x1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:  \\\\ \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture}   \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,-,0,+,d,+,0,-,}  \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-/$-\\infty$}  \n'
                                '\\end{tikzpicture}  \n'
                                '\\end{center} \n'
                                'Giá trị cực tiểu của hàm số là'
                                %(latex(x1),latex(x2),latex(x3),
                                latex(y1),latex(y2)
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
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Giá trị cực tiểu của hàm số là $y=%s$. \\\\ \n'
                        %(latex(y1),
                        ))
            if dang=='4':
                d = ['$y=%s$'%(latex(y2)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(x1)),
                    '$x=%s$'%(latex(y1)),
                    '$x=%s$'%(latex(y2)),
                    '$y=%s$'%(latex(x3)),
                    '$y=%s$'%(latex(y1)),
                    '$x=%s$'%(latex(x3)),
                    '$y=%s$'%(latex(x1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:  \\\\ \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture}   \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,-,0,+,d,+,0,-,}  \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-/$-\\infty$}  \n'
                                '\\end{tikzpicture}  \n'
                                '\\end{center} \n'
                                'Giá trị cực đại của hàm số là'
                                %(latex(x1),latex(x2),latex(x3),
                                latex(y1),latex(y2)
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
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Giá trị cực đại của hàm số là $y=%s$. \\\\ \n'
                        %(latex(y2),
                        ))
            if dang=='3':
                d = ['$x=%s$'%(latex(x3)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(x1)),
                    '$x=%s$'%(latex(y1)),
                    '$x=%s$'%(latex(y2)),
                    '$y=%s$'%(latex(x3)),
                    '$y=%s$'%(latex(y1)),
                    '$y=%s$'%(latex(y2)),
                    '$y=%s$'%(latex(x1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:  \\\\ \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture}   \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,-,0,+,d,+,0,-,}  \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-/$-\\infty$}  \n'
                                '\\end{tikzpicture}  \n'
                                '\\end{center} \n'
                                'Điểm cực đại của hàm số là'
                                %(latex(x1),latex(x2),latex(x3),
                                latex(y1),latex(y2)
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
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Điểm cực đại của hàm số là $x=%s$. \\\\ \n'
                        %(latex(x3),
                        ))
            if dang=='2':
                d = ['$x=%s$'%(latex(x1)),
                    ]
                da= random.choice(d)
                s = ['$x=%s$'%(latex(x3)),
                    '$x=%s$'%(latex(y1)),
                    '$x=%s$'%(latex(y2)),
                    '$y=%s$'%(latex(x3)),
                    '$y=%s$'%(latex(y1)),
                    '$y=%s$'%(latex(y2)),
                    '$y=%s$'%(latex(x1)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:  \\\\ \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture}   \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,-,0,+,d,+,0,-,}  \n'
                                '\\tkzTabVar{+/$+\\infty$,-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-/$-\\infty$}  \n'
                                '\\end{tikzpicture}  \n'
                                '\\end{center} \n'
                                'Điểm cực tiểu của hàm số là'
                                %(latex(x1),latex(x2),latex(x3),
                                latex(y1),latex(y2)
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
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Điểm cực tiểu của hàm số là $x=%s$. \\\\ \n'
                        %(latex(x1),
                        ))
            if dang=='1':
                d = ['Điểm cực đại của hàm số là $x=%s$'%(latex(x1)),
                    'Điểm cực tiểu của hàm số là $x=%s$'%(latex(x3)),
                    'Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$'%(latex(y1)),
                    'Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$'%(latex(y2)),
                    'Điểm cực đại của đồ thị hàm số là $(%s;%s)$'%(latex(x1),latex(y1)),
                    'Điểm cực tiểu của đồ thị hàm số là $(%s;%s)$'%(latex(x3),latex(y2)),
                    'Hàm số có hai điểm cực trị',
                    ]
                da= random.choice(d)
                s = ['Điểm cực đại của hàm số là $x=%s$'%(latex(x3)),
                    'Điểm cực tiểu của hàm số là $x=%s$'%(latex(x1)),
                    'Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$'%(latex(y2)),
                    'Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$'%(latex(y2+5)),
                    'Điểm cực đại của đồ thị hàm số là $(%s;%s)$'%(latex(x1),latex(y2)),
                    'Điểm cực tiểu của đồ thị hàm số là $(%s;%s)$'%(latex(x3),latex(y1)),
                    'Hàm số có một điểm cực trị',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:  \\\\ \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture}  \n'
                                    '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                                    '{$x$/0.7,$y\'$/0.7,$y$/2.1}  \n'
                                    '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                                    '\\tkzTabLine{,+,0,-,d,-,0,+,}  \n'
                                    '\\tkzTabVar{-/$-\\infty$,+/$%s$,-D+/$-\\infty$/$+\\infty$,-/$%s$,+/$+\\infty$}  \n'
                                '\\end{tikzpicture}  \n'
                                '\\end{center} \n'
                                'Khẳng định nào sau đây là đúng?'
                                %(latex(x1),latex(x2),latex(x3),
                                latex(y1),latex(y2)
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
                loigiai=(
                        'Từ bảng biến thiên ta có \\\\ \n'
                        '\\hspace*{1cm} Điểm cực đại của hàm số là $x=%s$. \\\\ \n'
                        '\\hspace*{1cm} Điểm cực tiểu của hàm số là $x=%s$. \\\\ \n'
                        '\\hspace*{1cm} Giá trị cực đại của hàm số là $y_{\\text{CĐ}}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Giá trị cực tiểu của hàm số là $y_{\\text{CT}}=%s$. \\\\ \n'
                        '\\hspace*{1cm} Điểm cực đại của đồ thị hàm số là $(%s;%s)$. \\\\ \n'
                        '\\hspace*{1cm} Điểm cực tiểu của đồ thị hàm số là $(%s;%s)$. \\\\ \n'
                        '\\hspace*{1cm} Hàm số có hai điểm cực trị. \\\\ \n'
                        %(latex(x1),
                        latex(x3),
                        latex(y1),
                        latex(y2),
                        latex(x1),latex(y1),
                        latex(x3),latex(y2),
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.0', '').replace('+1x', '+x').replace('-1x', '-x')
            return content

