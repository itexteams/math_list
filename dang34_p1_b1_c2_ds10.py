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


def bt_dang34_p1_b1_c2_ds10(self):
            #Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Bài toán: Miền nghiệm x - y < c không có điểm chung với bất phương trình nào dưới đây?
                # Ta sinh c1 > 0 cho bất phương trình gốc: x - y < c1
                c1 = randint(0, 3)

                # Đáp án đúng: x - y >= c2 với c2 > c1 (đảm bảo hai miền nghiệm x - y < c1 và x - y >= c2 là hai nửa mặt phẳng song song rời nhau hoàn toàn)
                c2 = c1 + randint(1, 4)
                da = '$x - y \\ge %s$' % (c2)

                # Các đáp án sai (có điểm chung với miền nghiệm x - y < c1):
                # Option 1: y < c3
                c3 = randint(-2, 2)
                das1 = '$y < %s$' % (c3)

                # Option 2: x >= c4
                c4 = randint(-2, 2)
                das2 = '$x \\ge %s$' % (c4)

                # Option 3: x - y < c5 với c5 > c1
                c5 = c1 + randint(1, 3)
                das3 = '$x - y < %s$' % (c5)

                # Câu hỏi
                if c1 == 0:
                    bpt_goc = 'x - y < 0'
                else:
                    bpt_goc = 'x - y < %s' % (c1)

                noidungcauhoi = ('Miền nghiệm của bất phương trình $%s$ \\textbf{không} có điểm chung với miền nghiệm của bất phương trình nào dưới đây?'
                                 % (bpt_goc))

                # Gắn thẻ đáp án đúng
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Tạo điểm chứng minh cho các đáp án sai có điểm chung
                # Cho y = c3 - 1, chọn x sao cho vừa thỏa x - y < c1 vừa thỏa y < c3
                x_test1 = c3 - 1 + c1 - 2
                y_test1 = c3 - 1

                # Cho x = c4 + 1, chọn y sao cho vừa thỏa x - y < c1 vừa thỏa x >= c4
                x_test2 = c4 + 1
                y_test2 = x_test2 - c1 + 2

                # Lời giải chi tiết
                loigiai = ('Xét đáp án chứa bất phương trình $x - y \\ge %s$: \\\\\n'
                           'Ta thấy miền nghiệm của bất phương trình $%s$ là tập hợp các điểm $(x; y)$ thỏa mãn $x - y < %s$. \\\\\n'
                           'Trong khi đó, miền nghiệm của bất phương trình $x - y \\ge %s$ là tập hợp các điểm $(x; y)$ thỏa mãn $x - y \\ge %s$. \\\\\n'
                           'Vì không tồn tại cặp số $(x; y)$ nào vừa thỏa mãn $x - y < %s$ vừa thỏa mãn $x - y \\ge %s$ (do %s < %s), nên hai miền nghiệm này hoàn toàn không có điểm chung. \\\\\n'
                           'Thử với các phương án còn lại: \\\\\n'
                           '- Với phương án $y < %s$, điểm $(%s; %s)$ vừa thỏa mãn $%s$ vừa thỏa mãn $y < %s$. \\\\\n'
                           '- Với phương án $x \\ge %s$, điểm $(%s; %s)$ vừa thỏa mãn $%s$ vừa thỏa mãn $x \\ge %s$. \\\\\n'
                           '- Với phương án $x - y < %s$, mọi điểm thuộc miền nghiệm của $%s$ đều thuộc miền nghiệm của $x - y < %s$. \\\\\n'
                           'Vậy đáp án đúng là $x - y \\ge %s$.'
                           % (c2, bpt_goc, c1, c2, c2, c1, c2, c1, c2, 
                              c3, x_test1, y_test1, bpt_goc, c3,
                              c4, x_test2, y_test2, bpt_goc, c4,
                              c5, bpt_goc, c5,
                              c2))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content


