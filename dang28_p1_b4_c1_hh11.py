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


def bt_dang28_p1_b4_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Ngân hàng các mệnh đề đúng và sai về quan hệ song song trong không gian
        menh_de_dung = [
            ('Hai mặt phẳng phân biệt không song song thì cắt nhau.', 'Hai mặt phẳng phân biệt không song song thì cắt nhau là khẳng định đúng theo tính chất vị trí tương đối của hai mặt phẳng.'),
            ('Nếu hai mặt phẳng song song với nhau thì mọi đường thẳng nằm trong mặt phẳng này đều song song với mặt phẳng kia.', 'Nếu $(P) // (Q)$ và $a \\subset (P)$ thì $a // (Q)$ là mệnh đề đúng.'),
            ('Qua một điểm nằm ngoài một mặt phẳng cho trước, có duy nhất một mặt phẳng song song với mặt phẳng đó.', 'Qua một điểm nằm ngoài một mặt phẳng, có duy nhất một mặt phẳng song song với mặt phẳng đã cho là mệnh đề đúng.')
        ]

        menh_de_sai = [
            ('Nếu hai mặt phẳng song song thì mọi đường thẳng nằm trên mặt phẳng này đều song song với mọi đường thẳng nằm trên mặt phẳng kia.', 'Nếu hai mặt phẳng song song thì hai đường thẳng lần lượt nằm trên hai mặt phẳng đó có thể chéo nhau hoặc song song, do đó mệnh đề này sai.'),
            ('Nếu hai mặt phẳng lần lượt chứa hai đường thẳng song song thì hai mặt phẳng này song song với nhau.', 'Hai mặt phẳng lần lượt chứa hai đường thẳng song song vẫn có thể cắt nhau (giao tuyến song song với hai đường thẳng đó), do đó mệnh đề này sai.'),
            ('Hai đường thẳng cùng song song với một mặt phẳng thì song song với nhau.', 'Hai đường thẳng cùng song song với một mặt phẳng có thể song song, cắt nhau hoặc chéo nhau, do đó mệnh đề này sai.')
        ]

        # Chọn ngẫu nhiên số lượng mệnh đề đúng (từ 0 đến 3)
        k = random.choice([0, 1, 2, 3])

        # Lấy k mệnh đề đúng và (3 - k) mệnh đề sai
        selected_dung = random.sample(menh_de_dung, k)
        selected_sai = random.sample(menh_de_sai, 3 - k)

        selected_all = selected_dung + selected_sai
        random.shuffle(selected_all)

        labels = ['(I)', '(II)', '(III)']
        list_md_str = []
        list_lg_str = []
        dung_labels = []

        for i in range(3):
            lbl = labels[i]
            text, reason = selected_all[i]
            list_md_str.append('%s: %s' % (lbl, text))
            list_lg_str.append('Mệnh đề %s: %s' % (lbl, reason))
            if selected_all[i] in selected_dung:
                dung_labels.append(lbl)

        md_I = list_md_str[0]
        md_II = list_md_str[1]
        md_III = list_md_str[2]

        lg_I = list_lg_str[0]
        lg_II = list_lg_str[1]
        lg_III = list_lg_str[2]

        # Kết luận số lượng mệnh đề đúng
        so_dung = k
        if so_dung == 0:
            ket_luan_dung = 'Không có mệnh đề nào đúng'
        elif so_dung == 1:
            ket_luan_dung = 'Mệnh đề %s đúng' % (dung_labels[0])
        elif so_dung == 2:
            ket_luan_dung = 'Các mệnh đề %s và %s đúng' % (dung_labels[0], dung_labels[1])
        else:
            ket_luan_dung = 'Cả ba mệnh đề %s, %s, %s đều đúng' % (labels[0], labels[1], labels[2])

        # Các đáp án trắc nghiệm
        da = '$%s$' % (so_dung)

        tap_so = [0, 1, 2, 3]
        tap_so.remove(so_dung)
        random.shuffle(tap_so)

        das1 = '$%s$' % (tap_so[0])
        das2 = '$%s$' % (tap_so[1])
        das3 = '$%s$' % (tap_so[2])

        # Câu hỏi
        noidungcauhoi = ('''Cho các mệnh đề sau:\\\\
    %s\\\\
    %s\\\\
    %s\\\\
    Có bao nhiêu mệnh đề đúng trong các mệnh đề trên?''' % (md_I, md_II, md_III))

        # Các đáp án
        da_d = ('\\True ' + str(da))
        da_s1 = str(das1)
        da_s2 = str(das2)
        da_s3 = str(das3)

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Xét từng mệnh đề:\\\\
    - %s\\\\
    - %s\\\\
    - %s\\\\
    %s.\\\\
    Vậy trong các mệnh đề đã cho có $%s$ mệnh đề đúng.''' % (lg_I, lg_II, lg_III, ket_luan_dung, so_dung))

    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\\choice \n' +
               '{' + str(list_1[0]) + '}\n' +
               '{' + str(list_1[1]) + '}\n' +
               '{' + str(list_1[2]) + '}\n' +
               '{' + str(list_1[3]) + '}\n' +
               '\\loigiai{' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content

