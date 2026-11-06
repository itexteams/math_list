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


def bt_dang15_p4_b3_c1_hh12(self):
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        R_radar = random.choice([20, 25, 30, 35, 40, 45, 50])
        x_tau = random.randint(10, 40)
        y_tau = random.randint(10, 30)
        z_tau = random.randint(-20, -5)
        d_binh = x_tau**2 + y_tau**2 + z_tau**2
        d = math.sqrt(d_binh)
        d_lam_tron = round(d, 1)
        if d_lam_tron == int(d_lam_tron):
            d_str = str(int(d_lam_tron))
        else:
            d_str = str(d_lam_tron).replace('.', ',')
        if d <= R_radar:
            ket_luan = f"Vì phạm vi theo dõi của ra đa là ${R_radar}$ km mà khoảng cách giữa ra đa và tàu thám hiểm là ${d_str}$ km nên ra đa phát hiện được tàu thám hiểm."
        else:
            ket_luan = f"Vì phạm vi theo dõi của ra đa là ${R_radar}$ km mà khoảng cách giữa ra đa và tàu thám hiểm là ${d_str}$ km nên ra đa không phát hiện được tàu thám hiểm."
        noidungcauhoi = f"Trong không gian, xét hệ toạ độ $Oxyz$ có gốc $O$ trùng với vị trí của một giàn khoan trên biển, mặt phẳng $(Oxy)$ trùng với mặt biển (được coi là phẳng) với trục $Ox$ hướng về phía tây, trục $Oy$ hướng về phía nam và trục $Oz$ hướng thẳng đứng lên trời. Đơn vị đo trong không gian $Oxyz$ lấy theo kilômét. Một chiếc ra đa đặt tại giàn khoan có phạm vi theo dõi là ${R_radar} \\text{{ km}}$. Một chiếc tàu thám hiểm có toạ độ là $({x_tau};{y_tau};{z_tau})$ đối với hệ toạ độ nói trên. Hỏi ra đa có phát hiện được tàu thám hiểm nói trên hay không?"
        loigiai = f"Để xác định xem ra đa có thể phát hiện được tàu thám hiểm hay không, ta cần xác định khoảng cách giữa ra đa và tàu thám hiểm.\\\\\nTheo đề ta có tọa độ của ra đa là $(0;0;0)$ tọa độ của tàu thám hiểm là $({x_tau};{y_tau};{z_tau})$. Khi đó khoảng cách giữa ra đa và tàu thám hiểm là:\\\\\n$d = \\sqrt{{({x_tau}-0)^2 + ({y_tau}-0)^2 + ({z_tau}-0)^2}} \\approx {d_str}$\\\\\n\\textbf{{Vậy:}}\\\\\n{ket_luan}"
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+
        '\n\\loigiai{ \n'
        +str(loigiai)+'\n}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

