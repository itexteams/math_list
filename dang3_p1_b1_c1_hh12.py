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


def bt_dang3_p1_b1_c1_hh12(self):
            # Khai báo biến
            lisdang=['8']
            dang=random.choice(lisdang)
            if dang=='8':
                a=randint(5,20)

                d = [
                    '$%s \\sqrt{3}$'%(latex(a)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(a+1)),
                    '$%s \\sqrt{2}$'%(latex(a+2)),
                    '$%s$'%(latex(a+3)),
                    '$%s \\sqrt{3}$'%(latex(a-1)),
                    '$%s \\sqrt{3}$'%(latex(a-2)),
                    '$%s \\sqrt{2}$'%(latex(a-3)),
                    '$%s$'%(latex(a-4)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian cho hình lập phương $ABCD.A\'B\'C\'D\'$ có tất cả các cạnh bằng $%s$. Độ dài vectơ $\\overrightarrow{AC\'}$ là  \n'
                                %(latex(a))
                                )


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
                        'Ta có \\\\ \n'
                        '$AC$ là đường chéo của $ABCD$ nên $AC=%s \\sqrt{2}$ \\\\ \n'
                        '$AC\'$ là đường chéo của $ACC\'A\'$ nên $AC\'=%s \\sqrt{3}$ \\\\ \n'
                        'Vậy $\\left| \\overrightarrow{AC\'} \\right| = AC\' =%s \\sqrt{3}$. \\\\ \n'                          
                        %(latex(a),latex(a),
                        latex(a))
                        )
            if dang=='7':
                a=randint(5,20)
                lisvt=['AC','CA','BD','DB','AB\'','BA\'','AD\'','DA\'','CD\'','DC\'']
                vt=random.choice(lisvt)
                d = [
                    '$%s \\sqrt{2}$'%(latex(a)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(a+1)),
                    '$%s \\sqrt{2}$'%(latex(a+2)),
                    '$%s$'%(latex(a+3)),
                    '$%s \\sqrt{3}$'%(latex(a-1)),
                    '$%s \\sqrt{3}$'%(latex(a-2)),
                    '$%s \\sqrt{2}$'%(latex(a-3)),
                    '$%s$'%(latex(a-4)),
                    ]
                d = [
                    '$7$',
                    ]
                da= random.choice(d)
                s = [
                    '$1$',
                    '$2$',
                    '$3$',
                    '$4$',
                    '$7$',
                    '$6$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian cho hình lập phương $ABCD.A\'B\'C\'D\'$ có tất cả các cạnh bằng $%s$. Độ dài vectơ $\\overrightarrow{%s}$ là  \n'
                                %(latex(a),str(vt))
                                )


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
                        'Ta có \\\\ \n'
                        '$%s$ là đường chéo của hình vuông nên $%s=%s \\sqrt{2}$ \\\\ \n'
                        'Vậy $\\left| \\overrightarrow{%s} \\right| = %s =%s \\sqrt{2}$. \\\\ \n'                          
                        %(str(vt),str(vt),latex(a),
                        str(vt),str(vt),latex(a))
                        )
            if dang=='6':
                a=randint(5,20)
                lisvt=['AB','BC','CD','DA','A\'B\'','B\'C\'','C\'D\'','D\'A\'','AA\'','BB\'','CC\'','DD\'']
                vt=random.choice(lisvt)
                d = [
                    '$%s$'%(latex(a)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(a+1)),
                    '$%s$'%(latex(a+2)),
                    '$%s$'%(latex(a+3)),
                    '$%s$'%(latex(a-1)),
                    '$%s$'%(latex(a-2)),
                    '$%s$'%(latex(a-3)),
                    '$%s$'%(latex(a-4)),
                    ]
                d = [
                    '$7$',
                    ]
                da= random.choice(d)
                s = [
                    '$1$',
                    '$2$',
                    '$3$',
                    '$4$',
                    '$7$',
                    '$6$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian cho hình lập phương $ABCD.A\'B\'C\'D\'$ có tất cả các cạnh bằng $%s$. Độ dài vectơ $\\overrightarrow{%s}$ là  \n'
                                %(latex(a),str(vt))
                                )


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
                        'Ta có \\\\ \n'
                        '$\\left| \\overrightarrow{%s} \\right| = %s =%s$. \\\\ \n'                          
                        %(str(vt),str(vt),latex(a))
                        )
            if dang=='5':
                a=randint(5,20)
                lisvt=['AB\'','AC\'','BC\'','BA\'','CA\'','CB\'']
                vt=random.choice(lisvt)
                d = [
                    '$%s \\sqrt{2}$'%(latex(a)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(a+1)),
                    '$%s \\sqrt{2}$'%(latex(a+2)),
                    '$%s$'%(latex(a+3)),
                    '$%s \\sqrt{3}$'%(latex(a-1)),
                    '$%s \\sqrt{3}$'%(latex(a-2)),
                    '$%s \\sqrt{2}$'%(latex(a-3)),
                    '$%s$'%(latex(a-4)),
                    ]
                d = [
                    '$4$',
                    ]
                da= random.choice(d)
                s = [
                    '$1$',
                    '$2$',
                    '$3$',
                    '$5$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian cho hình lăng trụ đứng $ABC.A\'B\'C\'$ có tất cả các cạnh bằng $%s$. Độ dài vectơ $\\overrightarrow{%s}$ là  \n'
                                %(latex(a),str(vt))
                                )

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
                        'Ta có \\\\ \n'
                        '$%s$ là đường chéo của hình vuông nên $%s=%s \\sqrt{2}$ \\\\ \n'
                        'Vậy $\\left| \\overrightarrow{%s} \\right| = %s =%s \\sqrt{2}$. \\\\ \n'                          
                        %(str(vt),str(vt),latex(a),
                        str(vt),str(vt),latex(a))
                        )
            if dang=='4':
                a=randint(5,20)
                lisvt=['AB','AC','BC','A\'B\'','A\'C\'','B\'C\'','AA\'','BB\'','CC\'']
                vt=random.choice(lisvt)
                d = [
                    '$%s$'%(latex(a)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(a+1)),
                    '$%s$'%(latex(a+2)),
                    '$%s$'%(latex(a+3)),
                    '$%s$'%(latex(a-1)),
                    '$%s$'%(latex(a-2)),
                    '$%s$'%(latex(a-3)),
                    '$%s$'%(latex(a-4)),
                    ]
                d = [
                    '$5$',
                    ]
                da= random.choice(d)
                s = [
                    '$1$',
                    '$2$',
                    '$3$',
                    '$4$',
                    '$7$',
                    '$6$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian cho hình lăng trụ đứng $ABC.A\'B\'C\'$ có tất cả các cạnh bằng $%s$. Độ dài vectơ $\\overrightarrow{%s}$ là  \n'
                                %(latex(a),str(vt))
                                ) 

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
                        'Ta có \\\\ \n'
                        '$\\left| \\overrightarrow{%s} \\right| = %s =%s$. \\\\ \n'                          
                        %(str(vt),str(vt),latex(a))
                        )
            if dang=='3':
                a=randint(5,20)
                lisvt=['AC','CA','BD','DB']
                vt=random.choice(lisvt)
                d = [
                    '$%s \\sqrt{2}$'%(latex(a)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(a+1)),
                    '$%s \\sqrt{2}$'%(latex(a+2)),
                    '$%s$'%(latex(a+3)),
                    '$%s \\sqrt{3}$'%(latex(a-1)),
                    '$%s \\sqrt{3}$'%(latex(a-2)),
                    '$%s \\sqrt{2}$'%(latex(a-3)),
                    '$%s$'%(latex(a-4)),
                    ]
                d = [
                    '$4$',
                    ]
                da= random.choice(d)
                s = [
                    '$1$',
                    '$2$',
                    '$3$',
                    '$5$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian cho hình chóp tứ giác đều $S.ABCD$ có tất cả các cạnh bằng $%s$. Độ dài vectơ $\\overrightarrow{%s}$ là  \n'
                                %(latex(a),str(vt))
                                ) 

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
                        'Ta có \\\\ \n'
                        'Đáy $ABCD$ là hình vuông nên $%s=%s \\sqrt{2}$ \\\\ \n'
                        'Vậy $\\left| \\overrightarrow{%s} \\right| = %s =%s \\sqrt{2}$. \\\\ \n'                          
                        %(str(vt),latex(a),
                        str(vt),str(vt),latex(a))
                        )
            if dang=='2':
                a=randint(5,20)
                lisvt=['SB','SB','SC','SD','AB','BC','CD','AD']
                vt=random.choice(lisvt)
                d = [
                    '$%s$'%(latex(a)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(a+1)),
                    '$%s$'%(latex(a+2)),
                    '$%s$'%(latex(a+3)),
                    '$%s$'%(latex(a-1)),
                    '$%s$'%(latex(a-2)),
                    '$%s$'%(latex(a-3)),
                    '$%s$'%(latex(a-4)),
                    ]
                d = [
                    '$4$',
                    ]
                da= random.choice(d)
                s = [
                    '$1$',
                    '$2$',
                    '$3$',
                    '$5$',
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian cho hình chóp $S.ABCD$ có tất cả các cạnh bằng $%s$. Độ dài vectơ $\\overrightarrow{%s}$ là  \n'
                                %(latex(a),str(vt))
                                ) 

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
                        'Ta có \\\\ \n'
                        '$\\left| \\overrightarrow{%s} \\right| = %s =%s$. \\\\ \n'                          
                        %(str(vt),str(vt),latex(a))
                        )
            if dang=='1':
                a=randint(5,20)
                lisvt=['AB','AC','AD','BC','BD','CD']
                vt=random.choice(lisvt)
                d = [
                    '$%s$'%(latex(a)),
                    ]
                da= random.choice(d)
                s = [
                    '$%s$'%(latex(a+1)),
                    '$%s$'%(latex(a+2)),
                    '$%s$'%(latex(a+3)),
                    '$%s$'%(latex(a-1)),
                    '$%s$'%(latex(a-2)),
                    '$%s$'%(latex(a-3)),
                    '$%s$'%(latex(a-4)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian cho tứ diện đều $ABCD$ có cạnh bằng $%s$. Độ dài vectơ $\\overrightarrow{%s}$ là  \n'
                                %(latex(a),str(vt))
                                ) 

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
                        'Ta có \\\\ \n'
                        '$\\left| \\overrightarrow{%s} \\right| = %s =%s$. \\\\ \n'                          
                        %(str(vt),str(vt),latex(a))
                        )


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n '+ str(noidungcauhoi)+ 
                '\\choice[2] \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

