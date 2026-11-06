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


def bt_dang52_p4_b1_c2_hh11(self):
            # Khai báo biến ký hiệu cạnh
            lis_a = ['a', 'x', 'm', 'b', 'c']
            val_a = random.choice(lis_a)

            # Chọn ngẫu nhiên giữa 2 dạng bài
            dang_bai = random.choice(['original', 'regular'])

            if dang_bai == 'original':
                # Dạng 1: Giống ảnh gốc - Kết quả 60 độ
                da_dung = '$60^\\circ$'

                noidungcauhoi = (f'Cho tứ diện $ABCD$ có $DA = DB = DC = AC = AB = {val_a}$, '
                                 f'$\\widehat{{ABC}} = 45^\\circ$. Tính góc giữa hai đường thẳng $AB$ và $DC$.')

                loigiai = (f'''Ta có tam giác $ABC$ có $AB=AC={val_a}$ và $\\widehat{{ABC}}=45^\\circ$ nên tam giác $ABC$ vuông cân tại $A$. \\\\
                             Suy ra $BC = AB\\sqrt{{2}} = {val_a}\\sqrt{{2}}$. \\\\
                             Xét tam giác $BDC$ có $DB^2 + DC^2 = {val_a}^2 + {val_a}^2 = 2{val_a}^2 = (BC)^2$. \\\\
                             Do đó tam giác $BDC$ vuông cân tại $D$, suy ra $\\vec{{DB}} \\cdot \\vec{{CD}} = 0$. \\\\
                             Ta có: $\\vec{{AB}} \\cdot \\vec{{CD}} = (\\vec{{DB}} - \\vec{{DA}}) \\cdot \\vec{{CD}} = \\vec{{DB}} \\cdot \\vec{{CD}} - \\vec{{DA}} \\cdot \\vec{{CD}} = 0 - \\vec{{DA}} \\cdot \\vec{{CD}}$. \\\\
                             Vì tam giác $ADC$ đều cạnh ${val_a}$ nên $(\\vec{{DA}}, \\vec{{CD}}) = 120^\\circ$. \\\\
                             $\\Rightarrow \\vec{{DA}} \\cdot \\vec{{CD}} = |\\vec{{DA}}| \\cdot |\\vec{{CD}}| \\cdot \\cos(120^\\circ) = {val_a} \\cdot {val_a} \\cdot \\left(-\\frac{{1}}{{2}}\\right) = -\\frac{{1}}{{2}}{val_a}^2$. \\\\
                             Do đó $\\vec{{AB}} \\cdot \\vec{{CD}} = \\frac{{1}}{{2}}{val_a}^2$. \\\\
                             Mặt khác: $\\cos(\\vec{{AB}}, \\vec{{CD}}) = \\frac{{\\vec{{AB}} \\cdot \\vec{{CD}}}}{{|\\vec{{AB}}| \\cdot |\\vec{{CD}}|}} = \\frac{{\\frac{{1}}{{2}}{val_a}^2}}{{{val_a} \\cdot {val_a}}} = \\frac{{1}}{{2}}$. \\\\
                             $\\Rightarrow (\\vec{{AB}}, \\vec{{CD}}) = 60^\\circ$. \\\\
                             Vậy góc giữa hai đường thẳng $AB$ và $DC$ bằng $60^\\circ$.''')

            else:
                # Dạng 2: Tứ diện đều - Kết quả 90 độ
                da_dung = '$90^\\circ$'

                noidungcauhoi = (f'Cho tứ diện đều $ABCD$ cạnh ${val_a}$. Tính góc giữa hai đường thẳng $AB$ và $DC$.')

                loigiai = (f'''Vì $ABCD$ là tứ diện đều nên tất cả các cạnh đều bằng ${val_a}$. \\\\
                             Xét tích vô hướng: $\\vec{{AB}} \\cdot \\vec{{CD}} = \\vec{{AB}} \\cdot (\\vec{{AD}} - \\vec{{AC}}) = \\vec{{AB}} \\cdot \\vec{{AD}} - \\vec{{AB}} \\cdot \\vec{{AC}}$. \\\\
                             Vì các mặt là tam giác đều nên $(\\vec{{AB}}, \\vec{{AD}}) = 60^\\circ$ và $(\\vec{{AB}}, \\vec{{AC}}) = 60^\\circ$. \\\\
                             $\\Rightarrow \\vec{{AB}} \\cdot \\vec{{AD}} = {val_a} \\cdot {val_a} \\cdot \\cos 60^\\circ = \\frac{{1}}{{2}}{val_a}^2$. \\\\
                             $\\Rightarrow \\vec{{AB}} \\cdot \\vec{{AC}} = {val_a} \\cdot {val_a} \\cdot \\cos 60^\\circ = \\frac{{1}}{{2}}{val_a}^2$. \\\\
                             Do đó $\\vec{{AB}} \\cdot \\vec{{CD}} = \\frac{{1}}{{2}}{val_a}^2 - \\frac{{1}}{{2}}{val_a}^2 = 0$. \\\\
                             Vì $\\vec{{AB}} \\cdot \\vec{{CD}} = 0$ nên $AB \\perp CD$. \\\\
                             Vậy góc giữa hai đường thẳng $AB$ và $DC$ bằng $90^\\circ$.''')

            # Điều chỉnh các phương án sai
            cac_lua_chon = ['$30^\\circ$', '$45^\\circ$', '$60^\\circ$', '$90^\\circ$', '$120^\\circ$']
            if da_dung in cac_lua_chon:
                cac_lua_chon.remove(da_dung)

            random.shuffle(cac_lua_chon)
            da_s1 = cac_lua_chon[0]
            da_s2 = cac_lua_chon[1]
            da_s3 = cac_lua_chon[2]

            # Trộn đáp án
            list_ans = ['\\True ' + str(da_dung), str(da_s1), str(da_s2), str(da_s3)]
            random.shuffle(list_ans)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')

            return content

