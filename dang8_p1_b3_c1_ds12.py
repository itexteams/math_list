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


def bt_dang8_p1_b3_c1_ds12(self):
            # Khai báo biến

            lisdang=['1','2','3','4','5','6','21','22','23','24','25']
            dang=random.choice(lisdang)
            if dang=='25':
                x1=randint(-9,9)
                i=randint(1,9)
                j=randint(1,9)
                x2=x1+i
                x3=x2+j
                k=randint(-9,9)
                h=randint(-9,9)
                tcn1=2*k
                tcn2=2*h+1
                y2=randint(-20,20)
                y3=randint(-20,20)
                listcn=[tcn1,tcn2]
                kq_tcn=random.choice(listcn)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:  \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,+,d,+,0,-,d,+}  \n'
                                '\\tkzTabVar{-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-D-/$%s$/$-\\infty$,+/$%s$}  \n'
                                '\\end{tikzpicture}  \n'
                                '\\end{center} \n'
                                'Đồ thị hàm số có số tiệm cận đứng là'
                                %(latex(x1),latex(x2),latex(x3),
                                latex(tcn1),latex(y2),latex(y3),latex(tcn2)

                                ))
                # Các đáp án
                da_d = '\\True $2$'
                da_s1 = '$3$'
                da_s2 = '$4$'
                da_s3 = '$1$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận đứng là $x=%s$ và $x=%s$.\\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận ngang là $y=%s$ và $y=%s$. \\\\ \n'
                        %(latex(x1),latex(x3),latex(tcn1),latex(tcn2))
                        )
            if dang=='24':
                x1=randint(-9,9)
                i=randint(1,9)
                j=randint(1,9)
                x2=x1+i
                x3=x2+j
                k=randint(-9,9)
                h=randint(-9,9)
                tcn1=2*k
                tcn2=2*h+1
                y2=randint(-20,20)
                y3=randint(-20,20)
                listcn=[tcn1,tcn2]
                kq_tcn=random.choice(listcn)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:   \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,+,d,+,0,-,d,+}  \n'
                                '\\tkzTabVar{-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-D-/$%s$/$-\\infty$,+/$%s$}  \n'
                                '\\end{tikzpicture}  \n'
                                '\\end{center} \n'
                                'Đồ thị hàm số có số tiệm cận ngang là'
                                %(latex(x1),latex(x2),latex(x3),
                                latex(tcn1),latex(y2),latex(y3),latex(tcn2)

                                ))
                # Các đáp án
                da_d = '\\True $2$'
                da_s1 = '$3$'
                da_s2 = '$4$'
                da_s3 = '$1$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận đứng là $x=%s$ và $x=%s$.\\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận ngang là $y=%s$ và $y=%s$. \\\\ \n'
                        %(latex(x1),latex(x3),latex(tcn1),latex(tcn2))
                        )
            if dang=='23':
                x1=randint(-9,9)
                i=randint(1,9)
                j=randint(1,9)
                x2=x1+i
                x3=x2+j
                k=randint(-9,9)
                h=randint(-9,9)
                tcn1=2*k
                tcn2=2*h+1
                y2=randint(-20,20)
                y3=randint(-20,20)
                listcn=[tcn1,tcn2]
                kq_tcn=random.choice(listcn)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:  \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,+,d,+,0,-,d,+}  \n'
                                '\\tkzTabVar{-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-D-/$%s$/$-\\infty$,+/$%s$}  \n'
                                '\\end{tikzpicture}  \n'
                                '\\end{center} \n'
                                'Đồ thị hàm số có số tiệm cận là'
                                %(latex(x1),latex(x2),latex(x3),
                                latex(tcn1),latex(y2),latex(y3),latex(tcn2)

                                ))
                # Các đáp án
                da_d = '\\True $4$'
                da_s1 = '$3$'
                da_s2 = '$2$'
                da_s3 = '$1$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận đứng là $x=%s$ và $x=%s$.\\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận ngang là $y=%s$ và $y=%s$. \\\\ \n'
                        %(latex(x1),latex(x3),latex(tcn1),latex(tcn2))
                        )

            if dang=='22':
                x1=randint(-9,9)
                i=randint(1,9)
                j=randint(1,9)
                x2=x1+i
                x3=x2+j
                k=randint(-9,9)
                h=randint(-9,9)
                tcn1=2*k
                tcn2=2*h+1
                y2=randint(-20,20)
                y3=randint(-20,20)
                listcn=[tcn1,tcn2]
                kq_tcn=random.choice(listcn)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:   \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,+,d,+,0,-,d,+}  \n'
                                '\\tkzTabVar{-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-D-/$%s$/$-\\infty$,+/$%s$}  \n'
                                '\\end{tikzpicture}  \n'
                                '\\end{center} \n'
                                'Đồ thị hàm số có một tiệm cận ngang là'
                                %(latex(x1),latex(x2),latex(x3),
                                latex(tcn1),latex(y2),latex(y3),latex(tcn2)

                                ))
                # Các đáp án
                da_d = '\\True $y=%s$' %(latex(kq_tcn))
                da_s1 = '$x=%s$' %(latex(kq_tcn+1))
                da_s2 = '$x=%s$' %(latex(kq_tcn+2))
                da_s3 = '$y=%s$' %(latex(kq_tcn-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận đứng là $x=%s$ và $x=%s$.\\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận ngang là $y=%s$ và $y=%s$. \\\\ \n'
                        %(latex(x1),latex(x3),latex(tcn1),latex(tcn2))
                        )

            if dang=='21':
                x1=randint(-9,9)
                i=randint(1,9)
                j=randint(1,9)
                x2=x1+i
                x3=x2+j
                k=randint(-9,9)
                h=randint(-9,9)
                tcn1=2*k
                tcn2=2*h+1
                y2=randint(-20,20)
                y3=randint(-20,20)
                listcd=[x1,x3]
                kq_tcd=random.choice(listcd)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:   \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5]  \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1}  \n'
                                '{$-\\infty$,$%s$,$%s$,$%s$,$+\\infty$}  \n'
                                '\\tkzTabLine{,+,d,+,0,-,d,+}  \n'
                                '\\tkzTabVar{-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-D-/$%s$/$-\\infty$,+/$%s$}  \n'
                                '\\end{tikzpicture}  \n'
                                '\\end{center} \n'
                                'Đồ thị hàm số có một tiệm cận đứng là'
                                %(latex(x1),latex(x2),latex(x3),
                                latex(tcn1),latex(y2),latex(y3),latex(tcn2)

                                ))
                # Các đáp án
                da_d = '\\True $x=%s$' %(latex(kq_tcd))
                da_s1 = '$x=%s$' %(latex(kq_tcd+1))
                da_s2 = '$x=%s$' %(latex(kq_tcd+2))
                da_s3 = '$y=%s$' %(latex(kq_tcd-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận đứng là $x=%s$ và $x=%s$.\\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận ngang là $y=%s$ và $y=%s$. \\\\ \n'
                        %(latex(x1),latex(x3),latex(tcn1),latex(tcn2))
                        )
            if dang=='6':
                x1=randint(-9,9)
                i=randint(1,9)
                x2=x1+i
                k=randint(-9,9)
                h=randint(-9,9)
                tcn1=2*k
                tcn2=2*h+1
                y2=randint(-20,20)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:   \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5] \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                '\\tkzTabLine{,+,d,+,0,-,} \n'
                                '\\tkzTabVar{-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-/$%s$}  \n'
                                '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Số đường tiệm cận đứng của đồ thị hàm số là'
                                %(latex(x1),latex(x2),
                                latex(tcn1),latex(y2),latex(tcn2)

                                ))
                # Các đáp án
                da_d = '\\True $1$'
                da_s1 = '$0$'
                da_s2 = '$3$'
                da_s3 = '$2$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận đứng là $x=%s$.\\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận ngang là $y=%s$ và $y=%s$. \\\\ \n'
                        %(latex(x1),latex(tcn1),latex(tcn2))
                        )

            if dang=='5':
                x1=randint(-9,9)
                i=randint(1,9)
                x2=x1+i
                k=randint(-9,9)
                h=randint(-9,9)
                tcn1=2*k
                tcn2=2*h+1
                y2=randint(-20,20)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:   \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5] \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                '\\tkzTabLine{,+,d,+,0,-,} \n'
                                '\\tkzTabVar{-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-/$%s$}  \n'
                                '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Số đường tiệm cận ngang của đồ thị hàm số là'
                                %(latex(x1),latex(x2),
                                latex(tcn1),latex(y2),latex(tcn2)

                                ))
                # Các đáp án
                da_d = '\\True $2$'
                da_s1 = '$0$'
                da_s2 = '$1$'
                da_s3 = '$3$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận đứng là $x=%s$.\\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận ngang là $y=%s$ và $y=%s$. \\\\ \n'
                        %(latex(x1),latex(tcn1),latex(tcn2))
                        )

            if dang=='4':
                x1=randint(-9,9)
                i=randint(1,9)
                x2=x1+i
                k=randint(-9,9)
                h=randint(-9,9)
                tcn1=2*k
                tcn2=2*h+1
                y2=randint(-20,20)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:   \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5] \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                '\\tkzTabLine{,+,d,+,0,-,} \n'
                                '\\tkzTabVar{-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-/$%s$}  \n'
                                '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Số đường tiệm cận của đồ thị hàm số là'
                                %(latex(x1),latex(x2),
                                latex(tcn1),latex(y2),latex(tcn2)

                                ))
                # Các đáp án
                da_d = '\\True $3$'
                da_s1 = '$0$'
                da_s2 = '$1$'
                da_s3 = '$2$'
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận đứng là $x=%s$.\\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận ngang là $y=%s$ và $y=%s$. \\\\ \n'
                        %(latex(x1),latex(tcn1),latex(tcn2))
                        )

            if dang=='3':
                x1=randint(-9,9)
                i=randint(1,9)
                x2=x1+i
                k=randint(-9,9)
                h=randint(-9,9)
                tcn1=2*k
                tcn2=2*h+1
                y2=randint(-20,20)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:  \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5] \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                '\\tkzTabLine{,+,d,+,0,-,} \n'
                                '\\tkzTabVar{-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-/$%s$}  \n'
                                '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Đồ thị hàm số có một tiệm cận ngang là'
                                %(latex(x1),latex(x2),
                                latex(tcn1),latex(y2),latex(tcn2)

                                ))
                # Các đáp án
                da_d = '\\True $y=%s$' %(latex(tcn2))
                da_s1 = '$x=%s$' %(latex(tcn2+1))
                da_s2 = '$x=%s$' %(latex(tcn2+2))
                da_s3 = '$y=%s$' %(latex(tcn2-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận đứng là $x=%s$.\\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận ngang là $y=%s$ và $y=%s$. \\\\ \n'
                        %(latex(x1),latex(tcn1),latex(tcn2))
                        )

            if dang=='2':
                x1=randint(-9,9)
                i=randint(1,9)
                x2=x1+i
                k=randint(-9,9)
                h=randint(-9,9)
                tcn1=2*k
                tcn2=2*h+1
                y2=randint(-20,20)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:   \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5] \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                '\\tkzTabLine{,+,d,+,0,-,} \n'
                                '\\tkzTabVar{-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-/$%s$}  \n'
                                '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Đồ thị hàm số có một tiệm cận ngang là'
                                %(latex(x1),latex(x2),
                                latex(tcn1),latex(y2),latex(tcn2)

                                ))
                # Các đáp án
                da_d = '\\True $y=%s$' %(latex(tcn1))
                da_s1 = '$x=%s$' %(latex(tcn1+1))
                da_s2 = '$x=%s$' %(latex(tcn1+2))
                da_s3 = '$y=%s$' %(latex(tcn1-1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận đứng là $x=%s$.\\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận ngang là $y=%s$ và $y=%s$. \\\\ \n'
                        %(latex(x1),latex(tcn1),latex(tcn2))
                        )

            if dang=='1':
                x1=randint(-9,9)
                i=randint(1,9)
                x2=x1+i
                k=randint(-9,9)
                h=randint(-9,9)
                tcn1=2*k
                tcn2=2*h+1
                y2=randint(-20,20)
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hàm số $y=f(x)$ có bảng biến thiên như sau:   \n'
                                '\\begin{center} \n'
                                '\\begin{tikzpicture} \n'
                                '\\tkzTabInit[espcl=3,lgt=1.5] \n'
                                '{$x$/0.7,$y\'$/0.7,$y$/2.1} \n'
                                '{$-\\infty$,$%s$,$%s$,$+\\infty$} \n'
                                '\\tkzTabLine{,+,d,+,0,-,} \n'
                                '\\tkzTabVar{-/$%s$,+D-/$+\\infty$/$-\\infty$,+/$%s$,-/$%s$}  \n'
                                '\\end{tikzpicture} \n'
                                '\\end{center} \n'
                                'Tiệm cận đứng của đồ thị hàm số là'
                                %(latex(x1),latex(x2),
                                latex(tcn1),latex(y2),latex(tcn2)

                                ))
                # Các đáp án
                da_d = '\\True $x=%s$' %(latex(x1))
                da_s1 = '$x=%s$' %(latex(x1-1))
                da_s2 = '$x=%s$' %(latex(x1-2))
                da_s3 = '$y=%s$' %(latex(x1+1))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Từ bảng biến thiên ta thấy \\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận đứng là $x=%s$.\\\\ \n'
                        '\\hspace*{1cm} Đồ thị hàm số có tiệm cận ngang là $y=%s$ và $y=%s$. \\\\ \n'
                        %(latex(x1),latex(tcn1),latex(tcn2))
                        )

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

