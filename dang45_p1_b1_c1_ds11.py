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


def bt_dang45_p1_b1_c1_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 + B3: Nghiên cứu đề bài và thiết lập random bài toán
                # Chọn ngẫu nhiên góc lượng giác của điểm M (thường là các góc đặc biệt: 30, 45, 60)
                goc_M = random.choice([30, 45, 60])

                # Chọn ngẫu nhiên trục đối xứng: 'Oy' hoặc 'Ox'
                truc_ds = random.choice(['Ox', 'Oy'])

                if truc_ds == 'Oy':
                    # Đối xứng qua Oy: sđ AN = (180 - goc_M) + k*360
                    goc_co_ban = 180 - goc_M
                    bu_hoac_doi = 'bù'
                else:
                    # Đối xứng qua Ox: sđ AN = -goc_M + k*360
                    goc_co_ban = -goc_M
                    bu_hoac_doi = 'đối'

                # Đáp án đúng dạng tổng quát lượng giác có đuôi + k360^\circ
                da = '$%d^\\circ + k360^\\circ, k \\in \\mathbb{Z}$' % goc_co_ban
                du = [da]
                da_chon = random.choice(du)

                # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                s = set()
                while len(s) < 3:
                    # Tạo phương án nhiễu chỉ lấy giá trị hình học (thiếu k360) hoặc sai góc cơ bản
                    sai_1 = '$%d^\\circ$' % goc_co_ban
                    sai_2 = '$%d^\\circ \\text{ hoặc } %d^\\circ$' % (goc_co_ban - 360, goc_co_ban + 120)
                    sai_3 = '$%d^\\circ + k360^\\circ, k \\in \\mathbb{Z}$' % (goc_M)
                    sai_4 = '$%d^\\circ$' % (-goc_co_ban)

                    for p_an in [sai_1, sai_2, sai_3, sai_4]:
                        if p_an != da:
                            s.add(p_an)

                list_sai = list(s)
                das1 = list_sai[0]
                das2 = list_sai[1]
                das3 = list_sai[2]

                # Câu hỏi
                noidungcauhoi = ('''Trên đường tròn lượng giác với điểm gốc là $A$. Điểm $M$ thuộc đường tròn sao cho cung lượng giác $AM$ có số đo $%s^\\circ$. Gọi $N$ là điểm đối xứng với điểm $M$ qua trục $%s$, số đo cung $AN$ là'''
                                 % (latex(goc_M), truc_ds))

                # Các đáp án
                da_d = ('\\True ' + str(da_chon))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết theo từng trường hợp hình học tương ứng
                if truc_ds == 'Oy':
                    giai_thich_goc = 'Cung $AM$ có số đo $%d^\\circ$ nên điểm $M$ ở vị trí góc $%d^\\circ$ trên đường tròn lượng giác. \\\\ Điểm $N$ đối xứng với $M$ qua trục tung $Oy$ nên điểm $N$ biểu diễn cho góc lượng giác có tính chất %s với góc ban đầu. \\\\ Do đó, một số đo hình học của cung $AN$ là $180^\\circ - %d^\\circ = %d^\\circ$.' % (goc_M, goc_M, bu_hoac_doi, goc_M, goc_co_ban)
                else:
                    giai_thich_goc = 'Cung $AM$ có số đo $%d^\\circ$ nên điểm $M$ ở vị trí góc $%d^\\circ$ trên đường tròn lượng giác. \\\\ Điểm $N$ đối xứng với $M$ qua trục hoành $Ox$ nên điểm $N$ biểu diễn cho góc lượng giác có tính chất %s với góc ban đầu. \\\\ Do đó, một số đo hình học của cung $AN$ là $-%d^\\circ$.' % (goc_M, goc_M, bu_hoac_doi, goc_M)

                loigiai = ('''%s \\\\
            Theo định nghĩa về số đo của cung lượng giác tổng quát, các cung lượng giác cùng tia đầu $A$ và tia cuối $ON$ sẽ hơn kém nhau một bội nguyên của một vòng quay ($360^\\circ$). \\\\
            Vậy số đo tổng quát của cung $AN$ là: $%d^\\circ + k360^\\circ, k \\in \\mathbb{Z}$.'''
                           % (giai_thich_goc, goc_co_ban))

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

