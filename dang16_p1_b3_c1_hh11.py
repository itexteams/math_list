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


def bt_dang16_p1_b3_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1', '2', '3']
    dang = random.choice(lisdang)

    # Ngẫu nhiên chọn tên các đường thẳng và mặt phẳng
    ten_duong = random.choice([('a', 'b'), ('d', 'd\''), ('m', 'n'), ('p', 'q')])
    ten_mp = random.choice(['\\alpha', 'P', 'Q', '\\beta'])
    d1, d2 = ten_duong[0], ten_duong[1]
    mp = ten_mp

    if dang == '1':
        # Dạng 1: Giống bài toán gốc - Cho d1 // d2 và d2 // (mp). Hỏi mệnh đề đúng liên quan đến d1 và (mp)
        # Đáp án đúng: d1 // (mp) hoặc d1 nằm trong (mp)
        noidungcauhoi = ('''Cho hai đường thẳng phân biệt $%s, %s$ và mặt phẳng $(%s)$. Giả sử $%s // %s$ và $%s // (%s)$. Mệnh đề nào sau đây \\textbf{đúng}?'''
                         % (d1, d2, mp, d1, d2, d2, mp))

        da = '$%s // (%s)$ hoặc $%s \\subset (%s)$' % (d1, mp, d1, mp)

        s = [
            '$%s // (%s)$' % (d1, mp),
            '$%s \\subset (%s)$' % (d1, mp),
            '$%s$ cắt $(%s)$' % (d1, mp),
            '$%s // (%s)$ và $%s \\subset (%s)$' % (d1, mp, d1, mp),
            '$%s$ chéo nhau với mọi đường thẳng nằm trong $(%s)$' % (d1, mp)
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        loigiai = ('''Vì $%s // (%s)$ nên $%s$ và $(%s)$ không có điểm chung. \\\\
    Mặt khác, hai đường thẳng $%s$ và $%s$ là hai đường thẳng phân biệt và $%s // %s$. \\\\
    Nếu $%s$ có điểm chung với $(%s)$ (giả sử là $M$), thì qua điểm $M$ có đường thẳng $%s // %s$, theo tiên đề Euclid về đường thẳng song song thì $%s$ phải nằm trọn trong $(%s)$ (mâu thuẫn nếu $%s$ cắt $(%s)$ tại duy nhất một điểm). \\\\
    Do đó, $%s$ chỉ có thể song song với $(%s)$ hoặc $%s$ nằm trong $(%s)$, tức là $%s // (%s)$ hoặc $%s \\subset (%s)$.'''
                   % (d2, mp, d2, mp, d1, d2, d1, d2, d1, mp, d1, d2, d1, mp, d1, mp, d1, mp, d1, mp, d1, mp, d1, mp))

    elif dang == '2':
        # Dạng 2: Hỏi mệnh đề SAI từ cùng một giả thiết d1 // d2 và d2 // (mp)
        # Khẳng định sai: d1 cắt (mp)
        noidungcauhoi = ('''Cho hai đường thẳng phân biệt $%s, %s$ và mặt phẳng $(%s)$. Giả sử $%s // %s$ và $%s // (%s)$. Mệnh đề nào sau đây \\textbf{sai}?'''
                         % (d1, d2, mp, d1, d2, d2, mp))

        da = '$%s$ cắt $(%s)$' % (d1, mp)

        s = [
            '$%s$ không thể cắt $(%s)$' % (d1, mp),
            '$%s // (%s)$ hoặc $%s \\subset (%s)$' % (d1, mp, d1, mp),
            '$%s$ có thể song song với $(%s)$' % (d1, mp),
            '$%s$ có thể nằm trong $(%s)$' % (d1, mp)
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        loigiai = ('''Theo tính chất vị trí tương đối giữa đường thẳng và mặt phẳng trong không gian: \\\\
    Vì $%s // %s$ và $%s // (%s)$ nên đường thẳng $%s$ không thể cắt mặt phẳng $(%s)$. \\\\
    Vị trí tương đối của $%s$ và $(%s)$ chỉ có thể là $%s // (%s)$ hoặc $%s \\subset (%s)$. \\\\
    Do đó, khẳng định "$%s$ cắt $(%s)$" là khẳng định sai.'''
                   % (d1, d2, d2, mp, d1, mp, d1, mp, d1, mp, d1, mp, d1, mp))

    elif dang == '3':
        # Dạng 3: Cho d1 // (mp), d2 // (mp) (hai đường phân biệt cùng song song với mp). Hỏi vị trí tương đối của d1 và d2
        noidungcauhoi = ('''Cho hai đường thẳng phân biệt $%s, %s$ và mặt phẳng $(%s)$. Giả sử $%s // (%s)$ và $%s // (%s)$. Vị trí tương đối giữa $%s$ và $%s$ có thể là'''
                         % (d1, d2, mp, d1, mp, d2, mp, d1, d2))

        da = 'Song song, cắt nhau hoặc chéo nhau'

        s = [
            'Song song với nhau',
            'Cắt nhau',
            'Chéo nhau',
            'Trùng nhau'
        ]

        das1 = random.choice(s)
        s.remove(das1)
        das2 = random.choice(s)
        s.remove(das2)
        das3 = random.choice(s)

        loigiai = ('''Hai đường thẳng phân biệt cùng song song với một mặt phẳng thì chúng có thể: \\\\
    - Song song với nhau: ví dụ hai đường thẳng song song thuộc một mặt phẳng song song với $(%s)$. \\\\
    - Cắt nhau: ví dụ hai đường thẳng cắt nhau thuộc một mặt phẳng song song với $(%s)$. \\\\
    - Chéo nhau: ví dụ hai đường thẳng chéo nhau nằm trong các mặt phẳng song song với $(%s)$. \\\\
    Do đó, giữa hai đường thẳng $%s$ và $%s$ có thể song song, cắt nhau hoặc chéo nhau.'''
                   % (mp, mp, mp, d1, d2))

    # Gán các phương án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2)
    da_s3 = str(das3)

    # Đưa các đáp án vào danh sách và xáo trộn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
        '\\choice \n'
        '{' + str(list_1[1]) + '}\n'
        '{' + str(list_1[2]) + '}\n'
        '{' + str(list_1[3]) + '}\n'
        '{' + str(list_1[0]) + '}\n'
        '\\loigiai{' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

