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


def bt_dang20_p1_b2_c2_hh11(self):
            # Khai báo biến
            # Khai báo các tập biến để random nhãn đường thẳng và mặt phẳng
            list_duong_thang = ['a', 'b', 'c', 'd']
            list_mat_phang = ['(P)', '(Q)', '(R)', '(\\alpha)', '(\\beta)', '(\\gamma)']

            # B3: Random nhãn cho bài toán
            dt_a = random.choice(list_duong_thang)
            list_duong_thang.remove(dt_a)
            dt_b = random.choice(list_duong_thang)
            mp_P = random.choice(list_mat_phang)

            # B4: Chuẩn bị các phương án (Đảm bảo logic hình học)
            # Khẳng định đúng (Nếu a // (P) và b vuông góc (P) thì b vuông góc a)
            da_dung = 'Nếu $%s // %s$ và $%s \\perp %s$ thì $%s \\perp %s$' % (dt_a, mp_P, dt_b, mp_P, dt_b, dt_a)

            # Các khẳng định sai
            sai1 = 'Nếu $%s // %s$ và $%s \\perp %s$ thì $%s \\perp %s$' % (dt_a, mp_P, dt_b, dt_a, dt_b, mp_P)
            sai2 = 'Nếu $%s \\perp %s$ và $%s \\perp %s$ thì $%s // %s$' % (dt_a, mp_P, dt_b, dt_a, dt_b, mp_P)
            sai3 = 'Nếu $%s // %s$ và $%s // %s$ thì $%s // %s$' % (dt_a, mp_P, dt_b, mp_P, dt_b, dt_a)

            # Câu hỏi
            noidungcauhoi = ('Cho hai đường thẳng phân biệt $%s, %s$ và mặt phẳng $%s$. Chọn khẳng định đúng?'
                             % (dt_a, dt_b, mp_P))

            # Gán nhãn True cho đáp án đúng để shuffle
            da_d = '\\True ' + da_dung
            da_s1 = sai1
            da_s2 = sai2
            da_s3 = sai3

            # Đưa các đáp án vào danh sách và xáo trộn
            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Nội dung lời giải chi tiết (B1 & B2) - Đã khớp đúng 26 biến %s
            loigiai = ('Vì đường thẳng $%s$ vuông góc với mặt phẳng $%s$ nên $%s$ vuông góc với mọi đường thẳng nằm trong mặt phẳng $%s$. \\\\ '
                       'Mặt khác, do đường thẳng $%s$ song song với mặt phẳng $%s$ nên tồn tại một đường thẳng $%s\'$ nằm trong mặt phẳng $%s$ sao cho $%s\' // %s$. \\\\ '
                       'Vì $%s \\perp %s$ nên $%s \\perp %s\'$. \\\\ '
                       'Từ $%s \\perp %s\'$ và $%s\' // %s$, theo tính chất cơ bản của quan hệ vuông góc và song song trong không gian, ta suy ra $%s \\perp %s$. \\\\ '
                       'Vậy khẳng định đúng là: Nếu $%s // %s$ và $%s \\perp %s$ thì $%s \\perp %s$.'
                       % (dt_b, mp_P, dt_b, mp_P, 
                          dt_a, mp_P, dt_a, mp_P, dt_a, dt_a, 
                          dt_b, mp_P, dt_b, dt_a, 
                          dt_b, dt_a, dt_a, dt_a, dt_b, dt_a, 
                          dt_a, mp_P, dt_b, mp_P, dt_b, dt_a))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choice \n'
                '{' + str(list_ans[0]) + '}\n'
                '{' + str(list_ans[1]) + '}\n'
                '{' + str(list_ans[2]) + '}\n'
                '{' + str(list_ans[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

