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


def bt_dang33_p3_b3_c4_ds11(self):
            # Khai báo biến
            # p1, p2, p3 là giá tiền gửi xe ở 3 định mức
            p1 = random.randint(3, 6) * 10000  # Từ 30k đến 60k
            p2 = p1 + random.randint(2, 5) * 10000 # p2 > p1
            p3 = p2 + random.randint(5, 10) * 10000 # p3 > p2

            # t1, t2 là các mốc thời gian chuyển đổi giá
            t1 = random.randint(1, 3)
            t2 = t1 + random.randint(2, 4)
            t_max = 24

            # Kết quả bài toán: Luôn có 2 điểm gián đoạn tại x = t1 và x = t2
            kq = 2

            # --- Các đáp án trắc nghiệm ---
            da_dung = '$%s$' % kq
            list_sai = ['$1$', '$3$', '$0$', '$4$']
            random.shuffle(list_sai)

            da_s1 = list_sai[0]
            da_s2 = list_sai[1]
            da_s3 = list_sai[2]

            # --- Nội dung câu hỏi ---
            noidungcauhoi = (r'''Một bãi đậu xe ô tô đưa ra giá $C(x)$ (đồng) khi thời gian đậu xe là $x$ (giờ) như sau:
            $$C(x) = \begin{cases} %s &\text{khi } 0 < x \le %s \\ %s &\text{khi } %s < x \le %s \\ %s &\text{khi } %s < x < %s \end{cases}$$
            Trên khoảng $(0; %s)$, hàm số $C(x)$ có bao nhiêu điểm gián đoạn?''' 
            % (p1, t1, p2, t1, t2, p3, t2, t_max, t_max))

            # --- Nội dung lời giải ---
            loigiai = (r'''Với $x$ thuộc các khoảng $(0; %s), (%s; %s), (%s; %s)$ thì hàm số $C(x)$ là hàm hằng nên hàm số liên tục. \\
            Xét tính liên tục của hàm số tại điểm $x = %s$: \\
            Vì $C(%s) = %s$ và $\lim_{x \to %s^-} C(x) = %s$, $\lim_{x \to %s^+} C(x) = %s$ nên hàm số không liên tục tại điểm $x = %s$. \\
            Xét tính liên tục của hàm số tại điểm $x = %s$: \\
            Vì $C(%s) = %s$ và $\lim_{x \to %s^-} C(x) = %s$, $\lim_{x \to %s^+} C(x) = %s$ nên hàm số không liên tục tại điểm $x = %s$. \\
            Vậy hàm số $C(x)$ liên tục trên mỗi khoảng $(0; %s), (%s; %s), (%s; %s)$ và nó gián đoạn tại hai điểm $x = %s, x = %s$.'''
            % (t1, t1, t2, t2, t_max,
               t1, t1, p1, t1, p1, t1, p2, t1,
               t2, t2, p2, t2, p2, t2, p3, t2,
               t1, t1, t2, t2, t_max, t1, t2))

            # --- Xuất câu trắc nghiệm theo định dạng ---
            da_d = ('\\True ' + str(da_dung))
            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(2))

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+ '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

