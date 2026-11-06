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


def bt_dang7_p3_b1_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(2,9)
                ik=Rational(a,2)
                ck=a*sqrt(3)/2 
                ic=ck
                gtri=(ik**2+ic**2-ck**2)/(2*ik*ic)

                gtri=1/a
                goc1=acos(gtri)
                gocz=goc1*180/pi

                h1=gocz
                number = Decimal(float(h1))  # Số cần làm tròn
                goc = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''                     
                                Cho tứ diện đều $ABCD$ cạnh $%s a$, gọi $I$ là trung điểm cạnh $AD$zz Góc giữa hai đường thẳng $AB$ và $CI$ là bao nhiêu? (làm tròn kết quả đến hàng phần chục)zz
                                '''
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1zz0cm,y=1zz0cm]
                        \\clip(-0zz9664065952232958,-2zz442286160107269) rectangle (5zz600937916847511,3zz655199557603996);
                        \\draw [line width=1zzpt] (0zz,0zz)-- (3zz,-2zz);
                        \\draw [line width=1zzpt] (3zz,-2zz)-- (5zz,0zz);
                        \\draw [line width=1zzpt] (5zz,0zz)-- (3zz,3zz);
                        \\draw [line width=1zzpt] (3zz,3zz)-- (0zz,0zz);
                        \\draw [line width=1zzpt] (3zz,3zz)-- (3zz,-2zz);
                        \\draw [line width=1zzpt] (4zz,1zz5)-- (3zz,-2zz);
                        \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (4zz,1zz5)-- (2zz5,0zz);
                        \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (2zz5,0zz)-- (3zz,-2zz);
                        \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,0zz)-- (5zz,0zz);
                        \\draw (2zz7,3zz516377641088678) node[anchor=north west] {$A$};
                        \\draw (-0zz6,0zz30211634331093606) node[anchor=north west] {$B$};
                        \\draw (2zz899249849280171,-1zz8976771030087147) node[anchor=north west] {$C$};
                        \\draw (2zz2,-0zz637601245408138) node[anchor=north west] {$O$};
                        \\draw (4zz041861008290864,1zz9893365594201826) node[anchor=north west] {$I$};
                        \\draw (2zz1197113950018474,0zz5370457404907046) node[anchor=north west] {$K$};
                        \\draw (5zz067007468711672,0zz32347356123636956) node[anchor=north west] {$D$};
                        \\begin{scriptsize}
                            \\draw [fill=black] (2zz721248771298776,-0zz8849950851951048) circle (1zz5pt);
                        \\end{scriptsize}
                \\end{tikzpicture}
            \\end{center}
                        Ta có các tam giác mặt đáy và mặt bên đều là tam giác đều cạnh $%s a$zz\\\\
                        Gọi $O$ là tâm tam giác $BDC$ và $K$ là trung điểm của $BD$ thì $IK$ là đường trung bình tam giác $ABD$, $IK//AB$zz \\\\
                        Rõ ràng $IC$ là trung tuyến đồng thời là đường cao tam giác $ACD$, $CK$ là đường cao tam giác đềuzz\\\\
                        Do đó $IK=\\dfrac{1}{2}AB=%s a$, $CK=IC=%s a$zz \\\\
                        Tam giác $CIK$ có $\\left(AB,CI\\right)=\\left(IK,CI\\right)=\\widehat{CIK}$zz\\\\
                        $\\cos \\widehat{CIK}=\\dfrac{IK^2+IC^2-CK^2}{2 IK \\cdot IC}=\\dfrac{%s a^2+%s a^2 -%s a^2}{2 \\cdot %s a \\cdot %s a}=%s$zz \\\\
                        suy ra $\\left(AB,CI\\right)=%s^\\circ$zz'''
                        %(latex(a),
                        latex(ik),latex(ck),
                        latex(ik**2),latex(ic**2),latex(ck**2),latex(ik),latex(ic),latex(gtri),
                        latex(goc)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(goc))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.')
            return content 

