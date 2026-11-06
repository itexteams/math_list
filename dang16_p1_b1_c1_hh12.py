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


def bt_dang16_p1_b1_c1_hh12(self):
            # Khai báo biến
            # Khai báo các vectơ dùng trong LaTeX
            vec_SA = '\\overrightarrow{SA}'
            vec_SB = '\\overrightarrow{SB}'
            vec_SC = '\\overrightarrow{SC}'
            vec_SD = '\\overrightarrow{SD}'
            vec_BA = '\\overrightarrow{BA}'
            vec_DC = '\\overrightarrow{DC}'
            vec_CD = '\\overrightarrow{CD}'  # <-- Đã thêm dòng này
            vec_AB = '\\overrightarrow{AB}'
            vec_AD = '\\overrightarrow{AD}'
            vec_AC = '\\overrightarrow{AC}'
            vec_BD = '\\overrightarrow{BD}'
            vec_BC = '\\overrightarrow{BC}'
            vec_CB = '\\overrightarrow{CB}'
            vec_DB = '\\overrightarrow{DB}'
            vec_CA = '\\overrightarrow{CA}'

            # Danh sách các dạng bài toán
            lisdang = ['1', '2', '3']
            dang = random.choice(lisdang)

            # Dạng 1: Bài toán gốc
            if dang == '1':
                # Đẳng thức đúng
                kq = f'${vec_SA} + {vec_SC} = {vec_SB} + {vec_SD}$'

                # Các đáp án sai
                s = [
                    f'${vec_SA} + {vec_SB} = {vec_SC} + {vec_SD}$',
                    f'${vec_SA} + {vec_SD} = {vec_SB} + {vec_SC}$',
                    f'${vec_AB} + {vec_AD} = {vec_BD}$',
                    f'${vec_SA} + {vec_SB} + {vec_SC} + {vec_SD} = \\overrightarrow{0}$',
                ]

                # Lời giải cho dạng 1
                loigiai = ('''Ta có, vì $ABCD$ là hình bình hành nên $\\overrightarrow{BA} = \\overrightarrow{CD}$.\\\\
            Áp dụng quy tắc cộng vectơ (quy tắc ba điểm):\\\\
            $\\overrightarrow{SA} = \\overrightarrow{SB} + \\overrightarrow{BA}$\\\\
            $\\overrightarrow{SC} = \\overrightarrow{SD} + \\overrightarrow{DC}$\\\\
            Cộng vế với vế: $\\overrightarrow{SA} + \\overrightarrow{SC} = (\\overrightarrow{SB} + \\overrightarrow{BA}) + (\\overrightarrow{SD} + \\overrightarrow{DC}) = \\overrightarrow{SB} + \\overrightarrow{SD} + (\\overrightarrow{BA} + \\overrightarrow{DC})$.\\\\
            Vì $\\overrightarrow{BA} + \\overrightarrow{DC} = \\overrightarrow{CD} + \\overrightarrow{DC} = \\overrightarrow{0}$, nên $\\overrightarrow{SA} + \\overrightarrow{SC} = \\overrightarrow{SB} + \\overrightarrow{SD}$.''')

            # Dạng 2: Tính chất đường chéo của hình bình hành
            elif dang == '2':
                # Đẳng thức đúng
                kq = f'${vec_AB} + {vec_AD} = {vec_AC}$'

                # Các đáp án sai
                s = [
                    f'${vec_AB} + {vec_BC} = {vec_AD}$',
                    f'${vec_AC} + {vec_BD} = \\overrightarrow{0}$',
                    f'${vec_AD} + {vec_DC} = {vec_CA}$',
                    f'${vec_BA} + {vec_BC} = {vec_DB}$'
                ]

                # Lời giải cho dạng 2
                loigiai = ('''Vì $ABCD$ là hình bình hành nên theo quy tắc hình bình hành, tổng của hai vectơ kề nhau xuất phát từ cùng một đỉnh bằng vectơ đường chéo xuất phát từ đỉnh đó.\\\\
            Vậy $\\overrightarrow{AB} + \\overrightarrow{AD} = \\overrightarrow{AC}$.''')

            # Dạng 3: Tổng vectơ đến các đỉnh của hình bình hành
            elif dang == '3':
                # Đẳng thức đúng
                kq = f'${vec_AB} + {vec_AD} + {vec_CB} + {vec_CD} = \\overrightarrow{0}$'

                # Các đáp án sai
                s = [
                    f'${vec_AB} + {vec_AD} + {vec_CB} + {vec_CD} = 2{vec_AC}$',
                    f'${vec_AB} + {vec_AD} + {vec_CB} + {vec_CD} = 2{vec_BD}$',
                    f'${vec_AB} + {vec_CD} = {vec_AC}$',
                    f'${vec_AD} + {vec_BC} = {vec_AC} + {vec_DB}$'
                ]

                # Lời giải cho dạng 3
                loigiai = ('''Ta có $\\overrightarrow{AB} + \\overrightarrow{CD} = \\overrightarrow{AB} - \\overrightarrow{AB} = \\overrightarrow{0}$ (vì $\\overrightarrow{CD} = - \\overrightarrow{AB}$ trong hình bình hành).\\\\
            Và $\\overrightarrow{AD} + \\overrightarrow{CB} = \\overrightarrow{AD} - \\overrightarrow{AD} = \\overrightarrow{0}$ (vì $\\overrightarrow{CB} = - \\overrightarrow{AD}$).\\\\
            Cộng vế với vế, ta được: $(\\overrightarrow{AB} + \\overrightarrow{CD}) + (\\overrightarrow{AD} + \\overrightarrow{CB}) = \\overrightarrow{0} + \\overrightarrow{0} = \\overrightarrow{0}$.\\\\
            Vậy đẳng thức đúng là $\\overrightarrow{AB} + \\overrightarrow{AD} + \\overrightarrow{CB} + \\overrightarrow{CD} = \\overrightarrow{0}$.''')


            # Phần tạo và xuất câu trắc nghiệm (chung cho tất cả các dạng)
            da_d = ('\\True ' + str(kq))
            du = [da_d]
            da = random.choice(du)

            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)

            noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Đẳng thức vectơ nào sau đây là đúng?''')

            list_1 = [da_d, das1, das2, das3]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\choice \n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '{' + str(list_1[0]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

