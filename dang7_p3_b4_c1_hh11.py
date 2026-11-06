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


def bt_dang7_p3_b4_c1_hh11(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Theo tính chất hình thang: AA' + CC' = BB' + DD' => DD' = AA' + CC' - BB'
        # Chọn ngẫu nhiên AA', CC', BB' sao cho DD' > 0 và các số nguyên đẹp
        bo_so = [
            (6, 10, 8, 4),
            (5, 9, 7, 3),
            (7, 11, 9, 5),
            (8, 12, 10, 6),
            (4, 8, 6, 2),
            (6, 9, 7, 4),
            (7, 10, 8, 5),
            (5, 8, 6, 3)
        ]
        aa, bb, cc, dd = random.choice(bo_so)
        tong_ac = aa + cc
        kq_str = str(dd)


        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình bình hành $ABCD$. Qua $A, B, C, D$ lần lượt vẽ các nửa đường thẳng $Ax, By, Cz, Dt$ ở cùng phía so với mặt phẳng $(ABCD)$, song song với nhau và không nằm trong $(ABCD)$. Một mặt phẳng $(P)$ cắt $Ax, By, Cz, Dt$ tương ứng tại $A', B', C', D'$ sao cho $AA' = %d$, $BB' = %d$, $CC' = %d$. Độ dài $DD'$ bằng bao nhiêu?'''
                         % (aa, bb, cc)
                         )

        # Nội dung lời giải
        loigiai = ('''\\begin{center}
        	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
        		\\draw [line width=1]    (345.97,240.67) -- (209.97,240.67) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (384.98,189.65) -- (248.98,189.65) ;
        		\\draw [line width=1]    (345.97,240.67) -- (384.98,189.65) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (209.97,240.67) -- (248.98,189.65) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (209.97,240.67) -- (384.98,189.65) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (345.97,240.67) -- (248.98,189.65) ;
        		\\draw [line width=1]    (209.97,64.34) -- (209.97,240.67) ;
        		\\draw [line width=1]    (345.97,64.34) -- (345.97,240.67) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (248.98,66.74) -- (248.98,189.65) ;
        		\\draw [line width=1]    (384.98,39.46) -- (384.98,189.65) ;
        		\\draw [line width=1]    (345.97,152.5) -- (209.73,117.75) ;
        		\\draw [line width=1]    (384.98,101.49) -- (248.74,66.74) ;
        		\\draw [line width=1]    (345.97,152.5) -- (384.98,101.49) ;
        		\\draw [line width=1]    (209.73,117.75) -- (248.74,66.74) ;
        		\\draw [line width=1]    (209.73,117.75) -- (384.98,101.49) ;
        		\\draw [line width=1]    (345.97,152.5) -- (248.74,66.74) ;
        		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (297.48,215.16) -- (297.36,109.62) ;
        		\\draw [line width=1]    (248.74,36.13) -- (248.74,66.74) ;
        		\\draw [line width=1]    (437.73,260.67) -- (143.73,260.67) ;
        		\\draw [line width=1]    (210.4,171.47) -- (143.73,260.67) ;
        		\\draw (149.33,242) node [anchor=north west][inner sep=0.75pt]    {$P)$};
        		\\draw (228,171.67) node [anchor=north west][inner sep=0.75pt]    {$A$};
        		\\draw (193.33,229) node [anchor=north west][inner sep=0.75pt]    {$B$};
        		\\draw (347.33,231) node [anchor=north west][inner sep=0.75pt]    {$C$};
        		\\draw (385.33,175) node [anchor=north west][inner sep=0.75pt]    {$D$};
        		\\draw (285.33,216) node [anchor=north west][inner sep=0.75pt]    {$O$};
        		\\draw (226,49.67) node [anchor=north west][inner sep=0.75pt]    {$A'$};
        		\\draw (190,105) node [anchor=north west][inner sep=0.75pt]    {$B'$};
        		\\draw (346,143.67) node [anchor=north west][inner sep=0.75pt]    {$C'$};
        		\\draw (386.67,87) node [anchor=north west][inner sep=0.75pt]    {$D'$};
        		\\draw (292.67,87) node [anchor=north west][inner sep=0.75pt]    {$O'$};
        		\\draw (220.67,95) node [anchor=north west][inner sep=0.75pt]    {$Q)$};
        	\\end{tikzpicture}
        \\end{center} Do $(P)$ cắt mặt phẳng $(Ax, By)$ theo giao tuyến $A'B'$ và cắt mặt phẳng $(Cz, Dt)$ theo giao tuyến $C'D'$, mà hai mặt phẳng $(Ax, By)$ và $(Cz, Dt)$ song song nên $A'B' // C'D'$.\\\\
    Tương tự có $A'D' // B'C'$ nên $A'B'C'D'$ là hình bình hành.\\\\
    Gọi $O, O'$ lần lượt là tâm $ABCD$ và $A'B'C'D'$. Dễ dàng có $OO'$ là đường trung bình của hai hình thang $AA'C'C$ và $BB'D'D$ nên $OO' = \\frac{AA' + CC'}{2} = \\frac{BB' + DD'}{2}$.\\\\
    Từ đó ta có $DD' = AA' + CC' - BB' = %d + %d - %d = %s$.\\\\
    Vậy $DD' = %s$.'''
                   % (aa, cc, bb, kq_str, kq_str)
                   )

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n' )
    return content

