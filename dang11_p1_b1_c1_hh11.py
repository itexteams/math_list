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


def bt_dang11_p1_b1_c1_hh11(self):
    # Khai báo các câu hỏi và đáp án đúng tương ứng
    xac_dinh_mp = [
        {
            'question': 'Một mặt phẳng hoàn toàn được xác định nếu biết điều kiện nào sau đây?',
            'correct': 'Ba điểm phân biệt không thẳng hàng',
        },
        {
            'question': 'Cách xác định mặt phẳng nào sau đây là đúng?',
            'correct': 'Một đường thẳng và một điểm không thuộc đường thẳng đó',
        },
        {
            'question': 'Để xác định duy nhất một mặt phẳng, ta cần biết điều kiện nào sau đây?',
            'correct': 'Hai đường thẳng cắt nhau',
        },
        {
            'question': 'Mặt phẳng được xác định duy nhất bởi điều kiện nào sau đây?',
            'correct': 'Hai đường thẳng song song',
        },
    ]

    # Random chọn một cách xác định mặt phẳng làm câu hỏi và đáp án đúng
    cau_hoi_chinh = random.choice(xac_dinh_mp)
    noidungcauhoi = cau_hoi_chinh['question']
    da_dung_text = cau_hoi_chinh['correct']
    da_d = '\\True ' + da_dung_text

    # Danh sách các mệnh đề SAI/nhiễu (tuyệt đối không chứa 4 cách xác định đúng)
    dap_an_sai = [
        'Hai đường thẳng phân biệt',
        'Ba điểm phân biệt bất kỳ',
        'Hai đường thẳng chéo nhau',
        'Bốn điểm phân biệt bất kỳ',
        'Một điểm và một đường thẳng bất kỳ',
        'Hai đường thẳng phân biệt vuông góc',
        'Ba điểm thẳng hàng',
        'Bốn điểm đồng phẳng',
        'Hai đường thẳng trùng nhau',
    ]

    # Lấy ngẫu nhiên 3 phương án sai
    s = random.sample(dap_an_sai, 3)
    das1, das2, das3 = s[0], s[1], s[2]

    # Đưa các đáp án vào danh sách và xáo trộn ngẫu nhiên vị trí A, B, C, D
    list_1 = [da_d, das1, das2, das3]
    random.shuffle(list_1)

    # Nội dung lời giải
    loigiai = (
        'Theo lý thuyết về cách xác định mặt phẳng trong hình học không gian, '
        'một mặt phẳng hoàn toàn được xác định khi biết một trong bốn điều kiện sau:\\\\\n'
        '(1) Ba điểm phân biệt không thẳng hàng.\\\\\n'
        '(2) Một đường thẳng và một điểm không thuộc đường thẳng đó.\\\\\n'
        '(3) Hai đường thẳng cắt nhau.\\\\\n'
        '(4) Hai đường thẳng song song.\\\\\n'
        'Do đó, trong các phương án đã cho, điều kiện đúng là: %s'
        % (da_dung_text)
    )

    # Xuất câu trắc nghiệm LaTeX
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

