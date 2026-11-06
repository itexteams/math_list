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


def bt_dang10_p3_b3_c1_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        while True:
            g = randint(6, 16)
            xa = randint(3, 8)
            ya = randint(9, 19)
            za = randint(3, 5)
            xv1 = randint(2, 5)
            yv1 = randint(2, 5)
            zv1 = randint(3, 5)
            h = randint(6, 12)
            xc = randint(140, 160)
            yc = randint(140, 160)
            zc = 0
            t1 = randint(2, 3)

            # Điều kiện để t0 nguyên đẹp
            if (h - za) % zv1 == 0 and h > za:
                t0 = Rational((h - za), zv1)
                xb = xa * 10 + xv1 * 100 * t0
                yb = ya * 10 + yv1 * 100 * t0
                zb = za + zv1 * t0
                xv2 = Rational((xc * 10 - xb), t1)
                yv2 = Rational((yc * 10 - yb), t1)
                zv2 = Rational((zc - zb), t1)
                break

        kq_sum = xv2 + yv2 + zv2
        x0 = kq_sum

        # Lấy tử số m và mẫu số n từ Rational đã tối giản
        m = kq_sum.p
        n = kq_sum.q
        kq = m + n

        # Nội dung câu hỏi
        noidungcauhoi = (
            '\\immini{'
            'Một chiếc máy bay đang bay trên không trung. Xét hệ trục tọa độ $Oxyz$ được gắn như hình vẽ, trong đó gốc $O$ là vị trí của trạm kiểm soát không lưu và gọi bộ số $(x;y;z)$ là tọa độ điểm biểu thị vị trí máy bay trên không trung. '
            'Biết các đơn vị trên các trục $Ox,Oy,Oz$ theo đơn vị km. Tại thời điểm $%s$h máy bay đang ở vị trí $A(%s;%s;%s)$ và chuyển động với vận tốc $\\vec{v_1}=(%s;%s;%s)$(km/h). '
            'Khi đạt độ cao $%s$km, máy bay ở vị trí $B$ thì máy bay đổi vận tốc mới là $\\vec{v_2}=(a;b;c)$, $a,b,c\\in \\mathbb{R}$ để hướng đến sân bay $C(%s;%s;%s)$. '
            'Biết rằng máy bay đó đến sân bay $C$ vào lúc $%s$h cùng ngày. Giả thiết máy bay đó khi bay trên từng chặng $AB$ và $BC$ là giữ nguyên vận tốc và hướng bay. Với $a+b+c=\\dfrac{m}{n}$ với $m\\in \\mathbb{Z};n\\in\\mathbb{N}^*;\\dfrac{m}{n}$ là phân số tối giản khi đó $m+n$ bằng bao nhiêu?'
            '}{'
            ''' \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,scale=0.7] 
                    \\clip(-2.6905513744327307,-1.7584152108403854) rectangle (7.126405699886344,4.094750663828045);
                    \\fill[line width=2.4pt,fill=black,fill opacity=1.0] (1.326086494580387,1.734686555642047) -- (1.2713741060765356,1.5220543185020787) -- (1.3472253719568748,1.5034023678757658) -- (1.3969639069603759,1.7172780683908215) -- cycle;
                    \\fill[line width=2.4pt,fill=black,fill opacity=1.0] (1.5,1.7) -- (1.4429720518386142,1.4785331003740152) -- (1.5101190740933406,1.4598811497477022) -- (1.5747791695978919,1.6799741671381956) -- cycle;
                    \\fill[line width=2.4pt,fill=black,fill opacity=1.0] (2.43713655266519,1.6795007794261116) -- (2.468575027016035,1.4982672214035888) -- (2.54624655188283,1.5075138315067786) -- (2.5101847724803896,1.6878227285189826) -- cycle;
                    \\fill[line width=2.4pt,fill=black,fill opacity=1.0] (2.6,1.7) -- (2.641486635945686,1.5186097636306066) -- (2.7200828218227997,1.5324796787853916) -- (2.6701511272655742,1.7100145927666384) -- cycle;
                    \\fill[line width=1.pt,fill=black,fill opacity=0.4000000059604645] (1.7887495531529962,2.3016995402860143) -- (1.9970512219000556,2.2884740375084234) -- (1.9987021945637644,2.13656476473048) -- (1.7533590994526869,2.1766689245082524) -- cycle;
                    \\fill[line width=1.pt,fill=black,fill opacity=0.4000000059604645] (1.9970512219000556,2.2884740375084234) -- (2.2110183345637355,2.304058608508235) -- (2.2676359718970613,2.1790279927304743) -- (1.9987021945637644,2.13656476473048) -- cycle;
                    \\draw [->,line width=1.pt,color=ffqqqq] (0.,0.) -- (5.,0.);
                    \\draw [->,line width=1.pt,color=ffqqqq] (0.,0.) -- (-2.4002830381449485,-1.6416957964552272);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (2.,-1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,-1.)-- (-1.427542492778904,-0.9763808985908512);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,-1.)-- (4.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,-1.)-- (2.,2.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (0.,3.);
                    \\draw [->,line width=1.pt] (0.,0.) -- (2.,2.);
                    \\draw [shift={(2.0095151688692043,2.106914808677667)},line width=1.pt]  plot[domain=3.4190259628515207:6.005751997917859,variable=\\t]({1.*0.4220394093124337*cos(\\t r)+0.*0.4220394093124337*sin(\\t r)},{0.*0.4220394093124337*cos(\\t r)+1.*0.4220394093124337*sin(\\t r)});
                    \\draw [shift={(2.245512561398377,1.9108319348737217)},line width=1.pt]  plot[domain=2.486410882820749:3.0168480577476746,variable=\\t]({1.*0.6469256367784375*cos(\\t r)+0.*0.6469256367784375*sin(\\t r)},{0.*0.6469256367784375*cos(\\t r)+1.*0.6469256367784375*sin(\\t r)});
                    \\draw [shift={(1.9651519997940028,1.9690943615273635)},line width=1.pt]  plot[domain=0.049328522835695894:0.8629942326115334,variable=\\t]({1.*0.4508128339253981*cos(\\t r)+0.*0.4508128339253981*sin(\\t r)},{0.*0.4508128339253981*cos(\\t r)+1.*0.4508128339253981*sin(\\t r)});
                    \\draw [shift={(1.996708034808246,2.2041672316213883)},line width=1.pt]  plot[domain=0.389808025793555:2.7769405338208046,variable=\\t]({1.*0.2827588630887244*cos(\\t r)+0.*0.2827588630887244*sin(\\t r)},{0.*0.2827588630887244*cos(\\t r)+1.*0.2827588630887244*sin(\\t r)});
                    \\draw [shift={(1.9912718005953862,3.8444365447317828)},line width=1.pt]  plot[domain=4.581860722988543:4.854090423125494,variable=\\t]({1.*1.5559732406424667*cos(\\t r)+0.*1.5559732406424667*sin(\\t r)},{0.*1.5559732406424667*cos(\\t r)+1.*1.5559732406424667*sin(\\t r)});
                    \\draw [shift={(2.0069217826608767,2.9573626156708777)},line width=1.pt]  plot[domain=4.398345664457505:5.035606543890667,variable=\\t]({1.*0.8208390059791635*cos(\\t r)+0.*0.8208390059791635*sin(\\t r)},{0.*0.8208390059791635*cos(\\t r)+1.*0.8208390059791635*sin(\\t r)});
                    \\draw [line width=1.pt] (1.7887495531529962,2.3016995402860143)-- (1.7533590994526869,2.1766689245082524);
                    \\draw [line width=1.pt] (2.2110183345637355,2.304058608508235)-- (2.2676359718970613,2.1790279927304743);
                    \\draw [line width=1.pt] (1.9970512219000556,2.2884740375084234)-- (1.9987021945637644,2.13656476473048);
                    \\draw [line width=1.pt] (1.603613874957258,1.9913232751927454)-- (-0.9829065194652593,2.1493307733607825);
                    \\draw [line width=1.pt] (1.7205131304899572,1.7993516691023461)-- (-0.9976361066857579,2.0901027300629704);
                    \\draw [line width=1.pt] (2.4154164627811516,1.9913232751927454)-- (5.006003798305261,2.113839339334056);
                    \\draw [line width=1.pt] (2.2917225679887245,1.793105556272669)-- (5.003455522882344,2.0512087695953944);
                    \\draw [line width=1.pt] (-1.038999182260345,2.200456676383874)-- (-1.2578317918430064,2.6046533787894943);
                    \\draw [line width=1.pt] (-1.2578317918430064,2.6046533787894943)-- (-1.062169693863215,2.1386686454428876);
                    \\draw [shift={(-0.9696523181789133,2.2202065059893377)},line width=1.pt]  plot[domain=3.4190447276580063:4.527518104430641,variable=\\t]({1.*0.07210439187298796*cos(\\t r)+0.*0.07210439187298796*sin(\\t r)},{0.*0.07210439187298796*cos(\\t r)+1.*0.07210439187298796*sin(\\t r)});
                    \\draw [shift={(-0.9673263050620017,2.1975364351613313)},line width=1.pt]  plot[domain=3.6970824265781785:4.437410271991111,variable=\\t]({1.*0.11162743867720441*cos(\\t r)+0.*0.11162743867720441*sin(\\t r)},{0.*0.11162743867720441*cos(\\t r)+1.*0.11162743867720441*sin(\\t r)});
                    \\draw [line width=1.pt] (5.306727241154692,2.584912354596775)-- (5.062802830345142,2.1574541562135945);
                    \\draw [line width=1.pt] (5.306727241154692,2.584912354596775)-- (5.0784691160655315,2.0932223847599962);
                    \\draw [shift={(4.986564475438312,2.197946670990098)},line width=1.pt]  plot[domain=4.9395257617541874:5.794944566019936,variable=\\t]({1.*0.08632456493852102*cos(\\t r)+0.*0.08632456493852102*sin(\\t r)},{0.*0.08632456493852102*cos(\\t r)+1.*0.08632456493852102*sin(\\t r)});
                    \\draw [shift={(4.997922441752275,2.1490615202230146)},line width=1.pt]  plot[domain=4.768873804221117:5.677002637358284,variable=\\t]({1.*0.09800905974542935*cos(\\t r)+0.*0.09800905974542935*sin(\\t r)},{0.*0.09800905974542935*cos(\\t r)+1.*0.09800905974542935*sin(\\t r)});
                    \\draw [line width=1.pt] (1.9432250919438425,2.481821962317249)-- (2.,3.8);
                    \\draw [line width=1.pt] (2.,3.8)-- (2.0480030000571503,2.4822344918217607);
                    \\draw [line width=1.pt] (2.1220088492738913,2.457647567248186)-- (3.4,2.6);
                    \\draw [line width=1.pt] (3.4,2.6)-- (2.2003498532101906,2.400337016382389);
                    \\draw [line width=1.pt] (1.8485142293721033,2.444980791633242)-- (0.6,2.6);
                    \\draw [line width=1.pt] (0.6,2.6)-- (1.796322006342895,2.403661628162022);
                    \\draw [line width=1.pt] (2.50086772305331,1.8130120284330764)-- (2.542657669744772,1.5993459270868202);
                    \\draw [line width=1.pt] (2.554018102865433,1.8180708908089147)-- (2.5989522294710126,1.608301881631549);
                    \\draw [line width=1.pt] (2.542657669744772,1.5993459270868202)-- (2.5989522294710126,1.608301881631549);
                    \\draw [line width=1.pt] (2.542657669744772,1.5993459270868202)-- (2.5989522294710126,1.608301881631549);
                    \\draw [line width=1.pt] (2.6,1.7)-- (2.641486635945686,1.5186097636306066);
                    \\draw [line width=1.pt] (2.6,1.7)-- (2.6701511272655742,1.7100145927666384);
                    \\draw [line width=1.pt] (2.6701511272655742,1.7100145927666384)-- (2.7200828218227997,1.5324796787853916);
                    \\draw [line width=1.pt] (2.7200828218227997,1.5324796787853916)-- (2.641486635945686,1.5186097636306066);
                    \\draw [line width=1.pt] (2.5101847724803896,1.6878227285189826)-- (2.54624655188283,1.5075138315067786);
                    \\draw [line width=1.pt] (2.5101847724803896,1.6878227285189826)-- (2.43713655266519,1.6795007794261116);
                    \\draw [line width=1.pt] (2.43713655266519,1.6795007794261116)-- (2.468575027016035,1.4982672214035888);
                    \\draw [line width=1.pt] (2.468575027016035,1.4982672214035888)-- (2.54624655188283,1.5075138315067786);
                    \\draw [line width=1.pt] (1.4989480814278864,1.823051719197287)-- (1.4531385493761155,1.5979055843824177);
                    \\draw [line width=1.pt] (1.4348076546883464,1.8299125997074261)-- (1.3916484958472637,1.6171212261101842);
                    \\draw [line width=1.pt] (1.3916484958472637,1.6171212261101842)-- (1.4531385493761155,1.5979055843824177);
                    \\draw [line width=1.pt] (1.5,1.7)-- (1.4429720518386142,1.4785331003740152);
                    \\draw [line width=1.pt] (1.4429720518386142,1.4785331003740152)-- (1.5101190740933406,1.4598811497477022);
                    \\draw [line width=1.pt] (1.5,1.7)-- (1.5747791695978919,1.6799741671381956);
                    \\draw [line width=1.pt] (1.5747791695978919,1.6799741671381956)-- (1.5101190740933406,1.4598811497477022);
                    \\draw [line width=1.pt] (1.3969639069603759,1.7172780683908215)-- (1.3472253719568748,1.5034023678757658);
                    \\draw [line width=1.pt] (1.3969639069603759,1.7172780683908215)-- (1.326086494580387,1.734686555642047);
                    \\draw [line width=1.pt] (1.326086494580387,1.734686555642047)-- (1.2713741060765356,1.5220543185020787);
                    \\draw [line width=1.pt] (1.2713741060765356,1.5220543185020787)-- (1.3472253719568748,1.5034023678757658);
                    \\draw [line width=2.4pt] (1.326086494580387,1.734686555642047)-- (1.2713741060765356,1.5220543185020787);
                    \\draw [line width=2.4pt] (1.2713741060765356,1.5220543185020787)-- (1.3472253719568748,1.5034023678757658);
                    \\draw [line width=2.4pt] (1.3472253719568748,1.5034023678757658)-- (1.3969639069603759,1.7172780683908215);
                    \\draw [line width=2.4pt] (1.3969639069603759,1.7172780683908215)-- (1.326086494580387,1.734686555642047);
                    \\draw [line width=2.4pt] (1.5,1.7)-- (1.4429720518386142,1.4785331003740152);
                    \\draw [line width=2.4pt] (1.4429720518386142,1.4785331003740152)-- (1.5101190740933406,1.4598811497477022);
                    \\draw [line width=2.4pt] (1.5101190740933406,1.4598811497477022)-- (1.5747791695978919,1.6799741671381956);
                    \\draw [line width=2.4pt] (1.5747791695978919,1.6799741671381956)-- (1.5,1.7);
                    \\draw [line width=2.4pt] (2.43713655266519,1.6795007794261116)-- (2.468575027016035,1.4982672214035888);
                    \\draw [line width=2.4pt] (2.468575027016035,1.4982672214035888)-- (2.54624655188283,1.5075138315067786);
                    \\draw [line width=2.4pt] (2.54624655188283,1.5075138315067786)-- (2.5101847724803896,1.6878227285189826);
                    \\draw [line width=2.4pt] (2.5101847724803896,1.6878227285189826)-- (2.43713655266519,1.6795007794261116);
                    \\draw [line width=2.4pt] (2.6,1.7)-- (2.641486635945686,1.5186097636306066);
                    \\draw [line width=2.4pt] (2.641486635945686,1.5186097636306066)-- (2.7200828218227997,1.5324796787853916);
                    \\draw [line width=2.4pt] (2.7200828218227997,1.5324796787853916)-- (2.6701511272655742,1.7100145927666384);
                    \\draw [line width=2.4pt] (2.6701511272655742,1.7100145927666384)-- (2.6,1.7);
                    \\draw [line width=1.pt] (2.997094864206994,1.7612952730854106) circle (0.09957006485380968cm);
                    \\draw [line width=1.pt] (0.9999494254705421,1.764014146315045) circle (0.11206992886367927cm);
                    \\draw [line width=1.pt] (4.,0.)-- (6.503098538854394,-1.604407300052416);
                    \\draw [line width=1.pt] (1.7887495531529962,2.3016995402860143)-- (1.9970512219000556,2.2884740375084234);
                    \\draw [line width=1.pt] (1.9970512219000556,2.2884740375084234)-- (1.9987021945637644,2.13656476473048);
                    \\draw [line width=1.pt] (1.9987021945637644,2.13656476473048)-- (1.7533590994526869,2.1766689245082524);
                    \\draw [line width=1.pt] (1.7533590994526869,2.1766689245082524)-- (1.7887495531529962,2.3016995402860143);
                    \\draw [line width=1.pt] (1.9970512219000556,2.2884740375084234)-- (2.2110183345637355,2.304058608508235);
                    \\draw [line width=1.pt] (2.2110183345637355,2.304058608508235)-- (2.2676359718970613,2.1790279927304743);
                    \\draw [line width=1.pt] (2.2676359718970613,2.1790279927304743)-- (1.9987021945637644,2.13656476473048);
                    \\draw [line width=1.pt] (1.9987021945637644,2.13656476473048)-- (1.9970512219000556,2.2884740375084234);
                    \\draw [line width=1.pt,color=ffqqqq] (-0.01391076518875708,-0.009514396582791294)-- (-0.0037655139548347094,1.9837918162463573);
                    \\draw [->,line width=1.pt,color=ffqqqq] (0.,2.122982941360237) -- (0.,3.987309503122941);
                    \\draw [line width=1.pt] (2.991888253461622,1.764054284153592) circle (0.07138713949611586cm);
                    \\draw [line width=1.pt] (0.9884746735825163,1.7614388617255514) circle (0.08270691916096162cm);
                    \\draw [->,line width=1.pt] (3.925494634956572E-4,-1.962747317478286E-4) -- (-0.5014390550773746,-0.34296388209918055);
                    \\draw [->,line width=1.pt] (3.925494634956572E-4,-1.962747317478286E-4) -- (0.7052902165365817,0.);
                    \\draw [->,line width=1.pt] (-0.01391076518875708,-0.009514396582791294) -- (-0.010299293315923035,0.7000559388966807);
                    \\draw (-2.5,-1.2) node[anchor=north west] {$x$};
                    \\draw (4.545558849990952,0.7) node[anchor=north west] {$y$};
                    \\draw (-0.6,4.1142287532612185) node[anchor=north west] {$z$};
                    \\draw (-0.8,0.4913041186910747) node[anchor=north west] {$O$};
                    \\draw (-0.5187444026339673,-0.14173378788704177) node[anchor=north west] {$\\vec{i}$};
                    \\draw (0.6207238292066395,0.7) node[anchor=north west] {$\\vec{j}$};
                    \\draw (-0.9,1.1827762935687096) node[anchor=north west] {$\\vec{k}$};
            \\end{tikzpicture}'''
            '}'
            % (
                latex(g), latex(xa * 10), latex(ya * 10), latex(za),
                latex(xv1 * 100), latex(yv1 * 100), latex(zv1),
                latex(h), latex(xc * 10), latex(yc * 10), latex(zc),
                latex(g + t0 + t1),
            )
        )

        # Nội dung lời giải
        loigiai = (
            'Gọi $t$(h) là thời gian bay từ vị trí $A(%s;%s;%s)$ đến vị trí $B(c;d;%s)$ - tại nơi có độ cao $%s$km.\\\\ \n'
            'Ta có $\\vec{OA}+t\\vec{v_1}=\\vec{OB}=(c;d;%s)$.\\\\ \n'
            '\\hspace*{1.17cm}$\\vec{OA}+t\\vec{v_1}=(%s+%st;%s+%st;%s+%st)$.\\\\ \n'
            'Suy ra $%s+%st=%s\\Leftrightarrow t=%s$\\\\ \n'
            'Khi đó $B(%s;%s;%s)$. Vậy tại thời điểm $%s$h cùng ngày, tọa độ của máy bay ở vị trí là $B(%s;%s;%s)$.\\\\ \n'
            'Vì máy bay đáp xuống sân bay $C(%s;%s;%s)$ vào lúc $%s$h cùng ngày nên thời gian bay từ vị trí $B(%s;%s;%s)$ (Máy bay ở độ cao $%s$km) đến $C(%s;%s;%s)$ là $%s$h.\\\\ \n'
            'Do đó $\\vec{OB}+%s\\vec{v_2}=\\vec{OC}=(%s;%s;%s)$.\\\\ \n'
            'Suy ra $\\vec{v_2}=\\left(%s;%s;%s\\right)$.\\\\ \n'
            'Vậy $a+b+c = %s \\Rightarrow m+n = %s$.'
            % (
                latex(xa * 10), latex(ya * 10), latex(za), latex(h), latex(h),
                latex(h),
                latex(xa * 10), latex(xv1 * 100), latex(ya * 10), latex(yv1 * 100), latex(za), latex(zv1),
                latex(za), latex(zv1), latex(h), latex(t0),
                latex(xb), latex(yb), latex(zb), latex(g + t0), latex(xb), latex(yb), latex(zb),
                latex(xc * 10), latex(yc * 10), latex(zc), latex(g + t0 + t1), latex(xb), latex(yb), latex(zb), latex(h), latex(xc * 10), latex(yc * 10), latex(zc), latex(t1),
                latex(t1), latex(xc * 10), latex(yc * 10), latex(zc),
                latex(xv2), latex(yv2), latex(zv2),
                latex(x0), latex(kq),
            )
        )

        # Đáp án
        dapan = ' \\shortans[0]{$%s$} ' % (latex(kq))

    # Xuất câu hỏi với đáp án và lời giải
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n'
        + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content

