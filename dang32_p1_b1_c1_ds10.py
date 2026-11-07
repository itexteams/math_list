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


def bt_dang32_p1_b1_c1_ds10(self):
        lisdang = ['1']
        dang = random.choice(lisdang)

        if dang == '1':
            danh_sach_ten = ['ABCD', 'XYZT', 'MNPQ', 'EFGH', 'UVXY']
            ten_tg = random.choice(danh_sach_ten)

            md_P = 'Tứ giác %s có cặp cạnh đối song song và bằng nhau' % (ten_tg)
            md_Q = 'Tứ giác %s là hình bình hành' % (ten_tg)

            da = 'Mệnh đề $P \\Leftrightarrow Q$ là: “%s là điều kiện cần và đủ để %s”' % (md_P, md_Q)

            s = [
                'Mệnh đề $P \\Leftrightarrow Q$ là: “%s suy ra %s”' % (md_P, md_Q),
                'Mệnh đề $P \\Leftrightarrow Q$ là: “%s là điều kiện cần để %s”' % (md_P, md_Q),
                'Mệnh đề $P \\Leftrightarrow Q$ là: “%s là điều kiện đủ để %s”' % (md_P, md_Q),
                'Mệnh đề $P \\Leftrightarrow Q$ là: “Nếu %s thì %s”' % (md_P, md_Q),
                'Mệnh đề $P \\Leftrightarrow Q$ là: “%s khi và chỉ khi %s”' % (md_Q, md_P)
            ]

            s = list(set(s))
            if da in s:
                s.remove(da)

            das1 = random.choice(s)
            s.remove(das1)
            das2 = random.choice(s)
            s.remove(das2)
            das3 = random.choice(s)

            noidungcauhoi = ('''Cho tứ giác $%s$. Xét mệnh đề $P$: “Tứ giác $%s$ có cặp cạnh đối song song và bằng nhau” và mệnh đề $Q$: “Tứ giác $%s$ là hình bình hành”. Mệnh đề $P \\Leftrightarrow Q$ là'''
                                % (latex(Symbol(ten_tg)), latex(Symbol(ten_tg)), latex(Symbol(ten_tg))))

            da_d = ('\\True ' + str(da))
            da_s1 = str(das1)
            da_s2 = str(das2)
            da_s3 = str(das3)

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            loigiai = ('''Mệnh đề $P \\Leftrightarrow Q$ là mệnh đề tương đương, được phát biểu dưới dạng “$P$ là điều kiện cần và đủ để $Q$” hoặc “$P$ khi và chỉ khi $Q$”. \\\\
Do đó, mệnh đề $P \\Leftrightarrow Q$ chính xác là: “Tứ giác $%s$ có cặp cạnh đối song song và bằng nhau là điều kiện cần và đủ để tứ giác $%s$ là hình bình hành”.'''
                        % (latex(Symbol(ten_tg)), latex(Symbol(ten_tg))))

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